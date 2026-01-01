# Novel Writing Workflow Guide

This guide explains the proper step-by-step workflow for writing a novel, from initial idea to finished manuscript.

## Overview: The 5-Phase Workflow

Novel writing works best when you follow this structured approach:

1. **Phase 1: Foundation** - Define your concept, goals, and basic story structure
2. **Phase 2: World Building** - Create settings, characters, and timeline BEFORE writing
3. **Phase 3: Outlining** - Plan your story in detail across all chapters
4. **Phase 4: Drafting** - Write your chapters using the outline as your guide
5. **Phase 5: Revision** - Review, refine, and polish your completed manuscript

**Important**: Don't skip phases! Each phase builds on the previous one.

---

# Phase 1: Foundation (Start Here)

## Step 1.1: Define Your Novel Basics

Before creating any files, answer these questions:

- **Genre**: What type of story? (fantasy, romance, mystery, sci-fi, literary fiction, etc.)
- **Target Length**: Most novels are 40,000-100,000 words
  - Literary/romance: 60,000-80,000 words
  - Fantasy/sci-fi: 80,000-120,000 words  
  - Mystery/thriller: 70,000-90,000 words
- **Story Concept**: One or two sentences describing your story
- **Target Audience**: Who will read this? (young adult, adult, etc.)

## Step 1.2: Update README.md

Update your project README with your decisions:

```bash
# Edit the README.md file with your information:
# - Genre
# - Target word count  
# - Current status
```

---

# Phase 2: World Building (Before Writing)

**This is where most beginners make mistakes - they start writing too soon! Build your world first.**

## Step 2.1: Create Your World Setting

**File**: `worldbuilding/locations/settings.md`

Describe where your story takes place:

```markdown
# World Settings

## Primary Setting
- **Location**: [City, village, world, etc.]
- **Time Period**: [Modern, historical, future, fantasy era]
- **Geography**: [Mountains, coastal, urban, rural, etc.]
- **Culture/Society**: [Social norms, government, technology level]
- **Climate**: [Weather patterns, seasons]

## Important Locations
1. **[Location Name]**: [Description and why it matters to the story]
2. **[Location Name]**: [Description and story relevance]
```

## Step 2.2: Develop Your Characters

**Create character profiles BEFORE writing any scenes.**

### Main Characters (Protagonists)
**File**: `worldbuilding/characters/protagonists.md`

```markdown
# [Character Name]

## Basic Info
- **Age**: 
- **Gender**:
- **Occupation**:
- **Physical Description**:

## Personality  
- **Strengths**:
- **Weaknesses**:
- **Fears**:
- **Desires**:
- **Quirks/Habits**:

## Background
- **Family**:
- **Education**:
- **Key Life Events**:
- **Traumas/Wounds**:

## Story Role
- **Goal**: [What do they want in the story?]
- **Motivation**: [Why do they want it?]
- **Conflict**: [What stops them?]
- **Character Arc**: [How do they change?]
```

### Opponents (Antagonists)
**File**: `worldbuilding/characters/antagonists.md`

Use the same format as protagonists. Remember: good antagonists have understandable motivations!

### Supporting Characters
**File**: `worldbuilding/characters/supporting.md`

Create simpler profiles for important secondary characters.

## Step 2.3: Establish Your Timeline

**File**: `worldbuilding/timeline.md`

```markdown
# Story Timeline

## Background Events (Before Story Starts)
- [Date/Period]: [Event that shapes the story world]

## Story Events  
- [Chapter 1-2 timeframe]: [Events that occur]
- [Chapter 3-5 timeframe]: [Events that occur]
- [Continuing for all chapters...]

## After Story (Optional)
- [Future events referenced or implied]
```

## Step 2.4: Gather Research (If Needed)

**File**: `research/notes.md`

Add any research needed for your story:
- Historical facts for historical fiction
- Technical details for sci-fi
- Cultural research for diverse settings
- Professional knowledge (medical, legal, etc.)

**Checkpoint**: ✅ Don't proceed to Phase 3 until you have:
- Complete world setting
- Character profiles for ALL major characters  
- Basic timeline established

---

# Phase 3: Outlining (Your Roadmap)

## Step 3.1: Create Your Story Structure

**File**: `manuscript/outline.md`

### Three-Act Structure

```markdown
# Novel Outline

## Act I: Setup (Chapters 1-4)
**Goal**: Introduce characters, setting, and the story problem

- **Opening Scene**: [How does the story begin?]
- **Inciting Incident**: [Event that launches the main story]
- **Plot Point 1**: [Point of no return - protagonist must engage with the problem]

## Act II: Conflict (Chapters 5-10)  
**Goal**: Complications, character development, raising stakes

- **First Half**: [Protagonist tries to solve problem, faces obstacles]
- **Midpoint**: [Major twist or revelation that changes everything]
- **Second Half**: [Stakes raised, timeline compressed, things get worse]

## Act III: Resolution (Chapters 11-15)
**Goal**: Climax and resolution

- **Climax**: [Final confrontation or ultimate test]
- **Resolution**: [Aftermath, showing how characters changed]
- **New Normal**: [How the world is different now]
```

## Step 3.2: Chapter-by-Chapter Breakdown

Expand your outline with detailed chapter plans:

```markdown
## Chapter Outlines

### Chapter 1: [Title]
- **Purpose**: [What does this chapter accomplish?]
- **Plot Points**: 
  - [Event 1]
  - [Event 2]
  - [Event 3]
- **Characters**: [Who appears?]
- **Setting**: [Where does it take place?]
- **Chapter End Hook**: [What makes readers want to read chapter 2?]

### Chapter 2: [Title]
[Continue for all planned chapters...]
```

**Checkpoint**: ✅ Don't proceed to Phase 4 until you have:
- Complete story structure (all three acts)
- Chapter-by-chapter outline
- Clear purpose for each chapter

---

# Phase 4: Drafting (Write Your Novel)

**Now you can finally start writing!** Use your outline as your guide.

## Daily Writing Workflow

### Before Writing Each Chapter:

1. **Review your outline** for this chapter's purpose
2. **Review character profiles** of characters in this chapter
3. **Read previous chapter** to maintain continuity
4. **Check timeline** to ensure proper sequencing

### Writing Options:

#### Option A: Write Directly in Chapter Files
Create chapters in `manuscript/chapters/`:
```markdown
# Chapter 1: [Title]

[Your chapter content here]
```

#### Option B: Draft Scenes First  
Write rough drafts in `manuscript/scenes/drafts/` first, then refine into chapters.

### After Writing Each Chapter:

1. **Save your work**: 
   ```bash
   git add .
   git commit -m "Completed chapter 3 draft"
   ```

2. **Check your progress**:
   ```bash
   make count
   ```

3. **Update timeline** if events changed

4. **Update character profiles** if characters evolved

### Weekly Workflow:

1. **Write daily** (300-500 words per day is realistic)
2. **Compile weekly** to see full story flow:
   ```bash
   make compile
   ```
3. **Review character consistency**:
   ```bash
   make track
   ```

## Drafting Tips:

- **Don't edit while drafting** - just get the story down
- **Use placeholders** like `[RESEARCH NEEDED]` for missing details
- **Follow your outline** but stay flexible if better ideas emerge
- **Update your outline** when you make changes

---

# Phase 5: Revision (Polish Your Manuscript)

## Step 5.1: Complete Your First Draft

**Checkpoint**: ✅ Finish ALL chapters before revising. Don't revise as you go!

## Step 5.2: The Big Picture Review

1. **Compile your manuscript**:
   ```bash
   make compile
   ```

2. **Read through completely** without making edits
3. **Identify major issues**:
   - Plot holes
   - Character inconsistencies  
   - Timeline problems
   - Pacing issues

## Step 5.3: Structural Revision

Fix major issues:
- Rewrite chapters that don't work
- Add missing scenes
- Remove unnecessary content
- Fix plot holes

## Step 5.4: Character Consistency Check

1. **Track character appearances**:
   ```bash
   make track
   ```

2. **Review each character's arc** - do they change consistently?
3. **Update character profiles** to match final versions

## Step 5.5: Line-by-Line Revision

Polish your prose:
- Fix awkward sentences
- Improve dialogue
- Enhance descriptions
- Check word choice

## Step 5.6: Final Polish

- Spell check
- Grammar check  
- Format consistency
- Get feedback from beta readers

---

# Essential Tools & Commands

## Track Your Progress

```bash
make count      # Check word count and progress
make compile    # Create full manuscript for review  
make track      # Check character appearances
make help       # See all available commands
make clean      # Remove compiled files (start fresh)
```

## Save Your Work

```bash
# Save current progress
git add .
git commit -m "Descriptive message of what you did"

# Try experimental changes safely
git checkout -b experiment-branch
[make your experimental changes]
git checkout main  # Return to main version

# See what you've changed
git status
```

---

# Project Structure Reference

## Planning Files (Prepare These First)
- `worldbuilding/locations/settings.md` - WHERE your story happens
- `worldbuilding/characters/protagonists.md` - WHO your story is about  
- `worldbuilding/characters/antagonists.md` - Who opposes your protagonist
- `worldbuilding/characters/supporting.md` - Secondary characters
- `worldbuilding/timeline.md` - WHEN events happen
- `research/notes.md` - Research and reference material

## Organizing Files (Create After Planning)
- `manuscript/outline.md` - WHAT happens in your story (detailed roadmap)
- `manuscript/chapters/` - Your actual novel chapters
- `manuscript/scenes/drafts/` - Rough drafts and scene experiments

## Generated Files (Automatic)
- `exports/compiled/` - Combined manuscripts (auto-generated)

---

# Common Troubleshooting

## "I'm stuck and don't know what to write"
1. Check your outline - you did create one, right?
2. Ask: "What does my character want RIGHT NOW?"
3. Write a rough scene in `drafts/` first
4. Skip ahead and come back later

## "My story is going in a different direction"
1. **Update your outline** to reflect the new direction
2. **Check character profiles** - are characters acting consistently?
3. **Update timeline** if events changed
4. **Save the old version** using git branches before making major changes

## "I forgot character details"
1. Review character profiles in `worldbuilding/characters/`
2. Use `make track` to see where characters appear
3. Read previous chapters with that character

## "I found a plot hole"
1. Don't panic - this is normal!
2. Update your outline to fix the structure
3. Add a note in the chapter: `[FIX: add scene showing X]`
4. Fix it during revision phase

---

# Milestones & Progress Tracking

## Preparation Milestones
- ✅ World setting complete
- ✅ All major character profiles created  
- ✅ Timeline established
- ✅ Complete outline finished
- ✅ Chapter-by-chapter breakdown done

## Writing Milestones  
- ✅ Chapter 1 complete
- ✅ Chapters 1-3 complete (Act I)
- ✅ 10,000 words total
- ✅ Chapters 1-8 complete (Act I & II)
- ✅ 25,000 words total
- ✅ All chapters drafted (First draft complete!)
- ✅ 40,000+ words (Novel length achieved)

## Revision Milestones
- ✅ First full read-through complete
- ✅ Major structural issues fixed
- ✅ Character consistency verified  
- ✅ Line-by-line revision complete
- ✅ Final polish done
- ✅ READY TO PUBLISH

---

# Quick Reference Checklist

## Before You Write ANYTHING:
- [ ] Genre and target length defined
- [ ] World setting documented
- [ ] All main characters profiled  
- [ ] Timeline established
- [ ] Complete outline created
- [ ] Chapter-by-chapter plan finished

## During Writing:
- [ ] Following outline for each chapter
- [ ] Checking character profiles before writing scenes
- [ ] Updating timeline as needed
- [ ] Saving progress daily with git commits
- [ ] Tracking word count weekly

## During Revision:
- [ ] Full manuscript compiled and read
- [ ] Structural issues identified and fixed
- [ ] Character consistency checked with `make track`
- [ ] Line-by-line polish completed
- [ ] Final proofreading done

---

**Remember**: Great novels are built on solid preparation. Take your time with Phases 1-3 - they will make writing and revision much easier!