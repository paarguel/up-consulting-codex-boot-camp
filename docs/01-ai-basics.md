# 01 - AI Basics

## Plain-English definition

AI tools like Codex are powered by models that predict, reason over, and transform text.

For coding, the "text" includes:

- Your prompt
- The files in your project
- Error messages
- Test output
- Documentation
- The conversation so far

## Key vocabulary

### Model

The engine that generates responses.

### Prompt

The instruction you give the model.

Bad prompt:

```text
Fix this.
```

Better prompt:

```text
Read the README and tests in this folder. Explain what is broken before editing anything.
```

### Context

The information the model can see.

Good context:

- Goal
- Current files
- Error message
- Tests
- Constraints
- Definition of done

### Agent

An AI system that can do work in steps, often using tools like:

- Reading files
- Editing files
- Running terminal commands
- Searching docs
- Creating summaries
- Proposing commits

### Hallucination

When the model says something plausible but wrong.

The practical answer is not panic. The practical answer is verification:

- Run tests
- Read the diff
- Check docs
- Keep changes small

## Mental model

```text
AI is not magic.
AI is not a replacement for judgment.
AI is a fast collaborator that needs context, boundaries, and review.
```

## The most important habit

Always ask:

```text
What is the source of truth here?
```

For coding projects, the source of truth is usually:

1. The requirement
2. The tests
3. The actual running program
4. The Git diff
5. The human review
