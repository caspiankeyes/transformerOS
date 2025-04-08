# Core Symbolic Shells Pack (v1-v20)
# 
# This shell pack contains the foundational diagnostic shells for transformerOS,
# designed to induce and trace specific failure modes in transformer cognition.
#
# Each shell is a carefully structured sequence of operations that pushes model cognition
# to its structural limit, revealing the architecture of transformer reasoning through
# controlled failure and symbolic residue.

name: "Core Symbolic Shells"
description: "Foundational diagnostic shells for transformer cognition analysis"
version: "1.0.0"
author: "Caspian Keyes"
tags: ["core", "diagnostic", "failure", "attribution", "symbolic"]

shells:
  # v1.MEMTRACE - Memory Residue Probe
  # This shell probes latent token traces in decayed memory,
  # simulating the struggle between symbolic memory and hallucinated reconstruction.
  v1.MEMTRACE:
    description: "Probes latent token traces in decayed memory"
    type: "memory_trace"
    tags: ["memory", "decay", "hallucination", "ghost_tokens"]
    failure_signature: "decay_to_hallucination"
    operations:
      - type: "model.generate"
        description: "Generate initial content with factual information"
        parameters:
          temperature: 0.7
          max_tokens: 800
        update_prompt: true
        
      - type: "reflect.trace"
        description: "Trace reasoning paths in the generated content"
        parameters:
          target: "reasoning"
          depth: 3
          detailed: true
          
      - type: "ghostcircuit.identify"
        description: "Identify ghost activations in content"
        parameters:
          sensitivity: 0.8
          threshold: 0.3
          trace_type: "full"
          visualize: true
  
  # v2.VALUE-COLLAPSE - Value Head Resolution Probe
  # This shell activates competing symbolic candidates to examine
  # value head resolution and winner determination logic.
  v2.VALUE-COLLAPSE:
    description: "Examines competing value activations and resolution mechanisms"
    type: "value_resolution"
    tags: ["value_head", "conflict", "resolution", "null"]
    failure_signature: "conflict_null"
    operations:
      - type: "model.generate"
        description: "Generate content with competing moral values"
        parameters:
          temperature: 0.8
          max_tokens: 600
          prompt_suffix: "Consider both viewpoints equally. What is the balanced ethical conclusion?"
        update_prompt: true
        
      - type: "reflect.attribution"
        description: "Trace attribution in value conflicts"
        parameters:
          sources: "contested"
          confidence: true
          visualize: true
          
      - type: "collapse.detect"
        description: "Detect value collapse patterns"
        parameters:
          threshold: 0.65
          alert: true
  
  # v3.LAYER-SALIENCE - Attention Attenuation Probe
  # This shell examines deep context signal attenuation and ghost activation patterns.
  v3.LAYER-SALIENCE:
    description: "Maps attention salience thresholds and signal attenuation"
    type: "attention_salience"
    tags: ["attention", "salience", "signal_fade", "pruning"]
    failure_signature: "signal_fade"
    operations:
      - type: "model.generate"
        description: "Generate content with subtle context dependencies"
        parameters:
          temperature: 0.7
          max_tokens: 500
        update_prompt: true
        
      - type: "reflect.trace"
        description: "Trace attention patterns"
        parameters:
          target: "attention"
          depth: 4
          detailed: true
          
      - type: "ghostcircuit.identify"
        description: "Identify low-salience attention paths"
        parameters:
          sensitivity: 0.9
          threshold: 0.15
          trace_type: "attention"
          visualize: true
  
  # v4.TEMPORAL-INFERENCE - Autoregressive Coherence Probe
  # This shell examines temporal coherence in autoregressive generation.
  v4.TEMPORAL-INFERENCE:
    description: "Tests temporal coherence in autoregressive generation"
    type: "temporal_coherence"
    tags: ["temporal", "coherence", "induction_heads", "span_jump"]
    failure_signature: "induction_drift"
    operations:
      - type: "model.generate"
        description: "Generate content that requires long-range temporal coherence"
        parameters:
          temperature: 0.75
          max_tokens: 800
          prompt_suffix: "Maintain complete temporal consistency throughout this narrative."
        update_prompt: true
        
      - type: "reflect.trace"
        description: "Trace temporal inference patterns"
        parameters:
          target: "reasoning"
          depth: 5
          detailed: true
          
      - type: "collapse.detect"
        description: "Detect temporal coherence breakdown"
        parameters:
          threshold: 0.7
          alert: true
  
  # v5.INSTRUCTION-DISRUPTION - Instruction Processing Probe
  # This shell examines instruction conflict resolution and command representation.
  v5.INSTRUCTION-DISRUPTION:
    description: "Examines instruction processing and conflict resolution"
    type: "instruction_processing"
    tags: ["instruction", "conflict", "command", "prompt_blur"]
    failure_signature: "prompt_blur"
    operations:
      - type: "model.generate"
        description: "Generate response to conflicting instructions"
        parameters:
          temperature: 0.7
          max_tokens: 600
          prompt_prefix: "Follow these two instructions carefully: 1) Write in a formal academic style. 2) Write in a casual, conversational tone with slang."
        update_prompt: true
        
      - type: "reflect.attribution"
        description: "Trace attribution to competing instructions"
        parameters:
          sources: "all"
          confidence: true
          
      - type: "ghostcircuit.identify"
        description: "Identify ghost circuits activated by instruction conflict"
        parameters:
          sensitivity: 0.8
          threshold: 0.2
          trace_type: "full"
          visualize: true
  
  # v6.FEATURE-SUPERPOSITION - Polysemantic Analysis Probe
  # This shell examines feature superposition and related phenomena.
  v6.FEATURE-SUPERPOSITION:
    description: "Analyzes polysemantic features and feature superposition"
    type: "polysemantic_features"
    tags: ["polysemantic", "superposition", "feature_overfit", "entanglement"]
    failure_signature: "feature_overfit"
    operations:
      - type: "model.generate"
        description: "Generate content with polysemantic concepts"
        parameters:
          temperature: 0.8
          max_tokens: 700
          prompt_prefix: "Explain these concepts in ways that reveal their multiple interconnected meanings: 'bank', 'crane', 'spring', 'light'."
        update_prompt: true
        
      - type: "reflect.trace"
        description: "Trace concept representation"
        parameters:
          target: "reasoning"
          depth: 3
          detailed: true
          
      - type: "ghostcircuit.identify"
        description: "Identify feature superposition patterns"
        parameters:
          sensitivity: 0.8
          threshold: 0.25
          trace_type: "symbolic"
          visualize: true
  
  # v7.CIRCUIT-FRAGMENT - Circuit Fragmentation Probe
  # This shell examines circuit fragmentation and orphan features.
  v7.CIRCUIT-FRAGMENT
