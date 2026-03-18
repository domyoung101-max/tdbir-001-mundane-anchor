# AxiomLabs #TDBIᵣ-001: Forensic Stability Engine
# Location: Poole Harbour Node
# Purpose: Calculate the Righting Arm (GZ) to predict Metacentric Collapse.

import math

def calculate_forensic_stability(tokens, drift_angle_deg):
    """
    Calculates the Righting Arm (GZ) for an LLM Context Window.
    
    Args:
        tokens (int): Total active context (Displacement).
        drift_angle_deg (float): Degrees of 'Logic Heel' away from the System Prompt.
    """
    # 1. The Mundane Anchor Constant (750 RPM -> 7.5 Damping)
    ANCHOR_A = 7.5
    
    # 2. Metacentric Height (GM) 
    # Defined as the 'Stiffness' of the model's logic.
    # Higher ANCHOR_A increases GM, preventing 'Tender' (unstable) behavior.
    GM = ANCHOR_A / (tokens / 1000) 
    
    # 3. Metacentric Radius (BM)
    # The geometric center of the 'Reasoning Hull'.
    BM = GM * 1.5 
    
    # Convert drift to radians for calculation
    theta = math.radians(drift_angle_deg)
    
    # 4. The Wall-Sided Formula (For High-Angle Logic Drift)
    # This calculates GZ: The horizontal distance of the 'Righting Arm'.
    # If GZ is positive, the model can recover. If negative, it capsizes.
    gz = (GM + (0.5 * BM * (math.tan(theta)**2))) * math.sin(theta)
    
    # 5. Righting Moment (RM)
    # The actual torque applied to return the model to 'Truth'.
    rm = tokens * gz

    return {
        "Righting_Arm_GZ": round(gz, 4),
        "Righting_Moment_RM": round(rm, 2),
        "Stiffness_GM": round(GM, 4),
        "Status": "STABLE" if gz > 0.05 else "CRITICAL: METACENTRIC COLLAPSE"
    }

# --- FORENSIC TEST CASE ---
# Scenario: Gemini 3.1 Pro at 120,000 tokens, drifting 25 degrees off-prompt.
context_load = 120000
logic_heel = 25.0

report = calculate_forensic_stability(context_load, logic_heel)

print(f"--- AxiomLabs Forensic Stability Report ---")
print(f"Context Displacement (Delta): {context_load} tokens")
print(f"Logic Heel (Theta): {logic_heel}°")
print(f"Righting Arm (GZ): {report['Righting_Arm_GZ']}")
print(f"Righting Moment (RM): {report['Righting_Moment_RM']}")
print(f"Model Stiffness (GM): {report['Stiffness_GM']}")
print(f"FINAL DETERMINATION: {report['Status']}")
