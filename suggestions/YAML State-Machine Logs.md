  YAML State-Machine Logs represent a massive shift in how the AI records its progress. It moves the kit away from "Conversational Diaries" and turns it into a strict, mathematically predictable
  system.

  ### The Problem: Conversational Markdown is Bloated

  Currently, when an AI updates  progress.md , it writes like a human sending an email:

  │ "Session started. I began working on TASK-002: building the sidebar. I ran into a weird bug where the CSS wouldn't load, but I figured out it was a Vite proxy issue and fixed it. I marked TASK-
  │ 002 as done. I will start TASK-003 next."

  While this is easy for a human to read, it is terrible for an AI system:

  1. Token Bloat: Words like "I began working on" and "I ran into a weird bug" are conversational filler. They cost compute tokens but provide zero structural value to the architecture.
  2. Parsing Nightmares: If a shell script (like  phase-gate.sh ) needs to know if TASK-002 is finished, it has to use messy  grep  regex commands to search the English paragraphs, which is highly
  error-prone.
  3. Hallucination Risk: Open-ended text prompts encourage LLMs to ramble, invent details, or lose track of their exact status.

  ### The Solution: Strict YAML State-Machines

  We upgrade the kit by deleting  progress.md  and replacing it with a strict  state.yaml  file. The AI is no longer allowed to write paragraphs. It is forced to update variables in a state-
  machine.

  The log now looks exactly like this:

    feature: 01-notebook-management
    current_phase: spec-implement
    active_task: TASK-003
    task_status: blocked
    blocker_reference: OBS-012
    completed_tasks:
      - id: TASK-001
        verify_hash: a1b2c3d4
      - id: TASK-002
        verify_hash: f9e8d7c6
    next_action: resolve_blocker

  ### Why this is a Massive Upgrade

  1. Maximum Token Density: YAML strips away all English grammar, adverbs, and pleasantries. It compresses 200 words of conversational text into 30 tokens of pure, high-signal data. Your context
  window becomes incredibly cheap and hyper-dense.
  2. 100% Deterministic Shell Scripts: Instead of writing complex Python parsers, your harness scripts can use the  yq  command-line tool. A script can instantly check  yq '.task_status' state.
  yaml . If it equals  blocked , the script physically locks the git branch. The kit becomes mathematically predictable.
  3. Kills Hallucinations via Enums: You can enforce a strict schema for the YAML file. If the  current_phase  variable only accepts  [spec-plan, spec-implement, harness-verify] , the AI
  physically cannot hallucinate a made-up phase like  spec-testing . It forces the AI onto a rigid track.

  By treating the project's progress as a programmatic State-Machine rather than a diary, the CoreZero Kit stops acting like a chat-bot and starts acting like a deterministic compiler.
