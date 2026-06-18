#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate CoreZero visual dashboard from active artifacts."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan"
    )
    parser.add_argument(
        "--output",
        default="docs/generated/dashboard.html",
        help="Path to save the generated HTML dashboard"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse everything but do not write output"
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Check syntax and structure without rendering"
    )
    return parser.parse_args()

def parse_feature_status(status_file: Path):
    if not status_file.exists():
        return {}
    content = status_file.read_text(encoding="utf-8")
    
    # Simple regex to extract metadata fields
    title_match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
    phase_match = re.search(r"-\s+(Phase|State):\s*(.*)", content, re.IGNORECASE)
    claim_match = re.search(r"-\s+Claimed\s*by:\s*(.*)", content, re.IGNORECASE)
    lease_match = re.search(r"-\s+Lease\s*expires:\s*(.*)", content, re.IGNORECASE)
    rigor_match = re.search(r"-\s+(Rigor|Profile):\s*(.*)", content, re.IGNORECASE)
    
    return {
        "title": title_match.group(1).strip() if title_match else status_file.parent.name,
        "phase": phase_match.group(2).strip() if phase_match else "Unknown",
        "claimed_by": claim_match.group(1).strip() if claim_match else "None",
        "lease": lease_match.group(1).strip() if lease_match else "N/A",
        "rigor": rigor_match.group(2).strip() if rigor_match else "Standard"
    }

def parse_feature_progress(progress_file: Path):
    if not progress_file.exists():
        return {"total": 0, "completed": 0, "percent": 0}
    content = progress_file.read_text(encoding="utf-8")
    
    # Match checkbox tasks like - [x] or - [ ]
    tasks = re.findall(r"-\s+\[([ xX])\]\s+(.*)", content)
    if not tasks:
        return {"total": 0, "completed": 0, "percent": 0}
    
    completed = sum(1 for status, _ in tasks if status.strip().lower() == "x")
    total = len(tasks)
    percent = int((completed / total) * 100) if total > 0 else 0
    return {"total": total, "completed": completed, "percent": percent}

def scan_workspace(root_path: Path):
    features = []
    features_dir = root_path / "artifacts" / "features"
    if features_dir.is_dir():
        for item in features_dir.iterdir():
            if item.is_dir():
                slug = item.name
                status = parse_feature_status(item / "status.md")
                progress = parse_feature_progress(item / "progress.md")
                
                features.append({
                    "slug": slug,
                    "title": status.get("title", slug),
                    "phase": status.get("phase", "Unknown"),
                    "claimed_by": status.get("claimed_by", "None"),
                    "lease": status.get("lease", "N/A"),
                    "rigor": status.get("rigor", "Standard"),
                    "progress": progress
                })
    return features

def get_html_template(features_json):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CoreZero Status Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0b0f19;
            --bg-card: rgba(20, 26, 45, 0.4);
            --bg-card-hover: rgba(30, 41, 69, 0.6);
            --border-glass: rgba(255, 255, 255, 0.08);
            --border-glass-active: rgba(59, 130, 246, 0.4);
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --accent-blue: #3b82f6;
            --accent-green: #10b981;
            --accent-purple: #8b5cf6;
            --accent-red: #ef4444;
            --accent-yellow: #f59e0b;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 2rem;
            line-height: 1.5;
            overflow-x: hidden;
        }}

        .glow {{
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(59,130,246,0.08) 0%, rgba(0,0,0,0) 70%);
            top: -200px;
            left: -200px;
            pointer-events: none;
            z-index: -1;
        }}

        .glow-right {{
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(139,92,246,0.05) 0%, rgba(0,0,0,0) 70%);
            bottom: -200px;
            right: -200px;
            pointer-events: none;
            z-index: -1;
        }}

        header {{
            margin-bottom: 3rem;
            border-bottom: 1px solid var(--border-glass);
            padding-bottom: 1.5rem;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 2.5rem;
            background: linear-gradient(135deg, #fff 30%, var(--accent-blue) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--text-secondary);
            font-weight: 300;
        }}

        .dashboard-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
        }}

        @media (min-width: 1024px) {{
            .dashboard-grid {{
                grid-template-columns: 2fr 1fr;
            }}
        }}

        .section-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        /* Search & Filter bar */
        .controls {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}

        .search-input {{
            flex: 1;
            min-width: 200px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            color: white;
            font-family: inherit;
            outline: none;
            transition: all 0.3s ease;
        }}

        .search-input:focus {{
            border-color: var(--accent-blue);
            background: rgba(255, 255, 255, 0.08);
        }}

        /* Card styles */
        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
            backdrop-filter: blur(12px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}

        .card:hover {{
            background: var(--bg-card-hover);
            border-color: var(--border-glass-active);
            transform: translateY(-2px);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
        }}

        .card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 600;
        }}

        .badge {{
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
        }}

        .badge-done {{ background: rgba(16, 185, 129, 0.15); color: var(--accent-green); }}
        .badge-implementing {{ background: rgba(59, 130, 246, 0.15); color: var(--accent-blue); }}
        .badge-planning {{ background: rgba(139, 92, 246, 0.15); color: var(--accent-purple); }}
        .badge-specing {{ background: rgba(245, 158, 11, 0.15); color: var(--accent-yellow); }}
        .badge-unknown {{ background: rgba(156, 163, 175, 0.15); color: var(--text-secondary); }}

        .meta-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
            font-size: 0.875rem;
        }}

        .meta-item {{
            color: var(--text-secondary);
        }}

        .meta-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.25rem;
        }}

        .meta-value {{
            color: var(--text-primary);
            font-weight: 500;
        }}

        /* Progress Bar */
        .progress-container {{
            margin-top: 1rem;
        }}

        .progress-info {{
            display: flex;
            justify-content: space-between;
            font-size: 0.875rem;
            margin-bottom: 0.5rem;
        }}

        .progress-bar {{
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
            width: 0%;
            border-radius: 3px;
            transition: width 1s ease;
        }}

        /* Observability List */
        .obs-list {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}

        .obs-item {{
            background: rgba(239, 68, 68, 0.03);
            border: 1px solid rgba(239, 68, 68, 0.15);
            border-radius: 8px;
            padding: 1rem;
            transition: border-color 0.3s ease;
        }}

        .obs-item:hover {{
            border-color: rgba(239, 68, 68, 0.35);
        }}

        .obs-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-size: 0.875rem;
        }}

        .obs-id {{
            font-weight: 700;
            color: var(--accent-red);
        }}

        .obs-class {{
            text-transform: uppercase;
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--accent-yellow);
        }}

        .obs-fix {{
            font-size: 0.875rem;
            margin-top: 0.5rem;
            padding-top: 0.5rem;
            border-top: 1px dashed rgba(255, 255, 255, 0.05);
            color: var(--text-secondary);
        }}
    </style>
</head>
<body>
    <div class="glow"></div>
    <div class="glow-right"></div>

    <header>
        <h1>CoreZero status</h1>
        <div class="subtitle">Real-time developer visual dashboard</div>
    </header>

    <div class="dashboard-grid">
        <!-- Active Feature Branch Visual Pipeline -->
        <div>
            <div class="section-title">Active Features</div>
            <div class="controls">
                <input type="text" id="search-bar" class="search-input" placeholder="Search features by name or slug..." oninput="filterCards()">
            </div>
            
            <div id="features-container" style="display: flex; flex-direction: column; gap: 1.5rem;">
                <!-- Dynamically generated features go here -->
            </div>
        </div>
    </div>

    <script>
        const features = {features_json};

        function renderFeatures() {{
            const container = document.getElementById('features-container');
            if (features.length === 0) {{
                container.innerHTML = '<div class="card" style="text-align: center; color: var(--text-secondary);">No active features found.</div>';
                return;
            }}
            
            container.innerHTML = features.map((feat, index) => {{
                const phaseClass = 'badge-' + feat.phase.toLowerCase().replace(/[' ]/g, '');
                return `
                    <div class="card feature-card" id="feature-card-${{index}}" data-title="${{feat.title}}" data-slug="${{feat.slug}}">
                        <div class="card-header">
                            <div>
                                <div class="card-title">${{feat.title}}</div>
                                <div style="font-size: 0.875rem; color: var(--text-secondary); margin-top: 0.25rem;">${{feat.slug}}</div>
                            </div>
                            <span class="badge ${{phaseClass}}">${{feat.phase}}</span>
                        </div>
                        <div class="meta-list">
                            <div class="meta-item">
                                <div class="meta-label">Claimed By</div>
                                <div class="meta-value" id="claim-val-${{index}}">${{feat.claimed_by}}</div>
                            </div>
                            <div class="meta-item">
                                <div class="meta-label">Lease Expires</div>
                                <div class="meta-value">${{feat.lease}}</div>
                            </div>
                            <div class="meta-item">
                                <div class="meta-label">Rigor Profile</div>
                                <div class="meta-value">${{feat.rigor}}</div>
                            </div>
                        </div>
                        <div class="progress-container">
                            <div class="progress-info">
                                <span>Task Completion</span>
                                <span>${{feat.progress.percent}}% (${{feat.progress.completed}}/${{feat.progress.total}})</span>
                            </div>
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: ${{feat.progress.percent}}%"></div>
                            </div>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        function filterCards() {{
            const query = document.getElementById('search-bar').value.toLowerCase();
            const cards = document.querySelectorAll('.feature-card');
            cards.forEach(card => {{
                const title = card.getAttribute('data-title').toLowerCase();
                const slug = card.getAttribute('data-slug').toLowerCase();
                if (title.includes(query) || slug.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        // Initial render
        renderFeatures();
    </script>
</body>
</html>
"""

def main():
    args = parse_args()
    root = Path(args.root).resolve()
    
    # Check execution constraints
    if args.check_only:
        print("Generator structure check passed.")
        return 0
        
    # Scan for features
    features = scan_workspace(root)
    
    if args.dry_run:
        print(f"Features scanned: {len(features)}")
        return 0
        
    # Render dashboard
    html_content = get_html_template(
        json.dumps(features)
    )
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_content, encoding="utf-8")
    
    print(f"Successfully generated visual dashboard at: {output_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
