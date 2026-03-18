# AxiomLabs #TDBIᵣ-001 | Live Testing Node: Poole Harbour
# Stress Test: Variable RPM Throttle vs. High Token Displacement

import math

def run_throttle_test(tokens, rpm_setting, drift_angle):
    # Convert RPM to the Anchor Constant (A)
    # 750 RPM = 7.5 | 1200 RPM = 12.0 | 2500 RPM = 25.0
    anchor_a = rpm_setting / 100
    
    # Calculate GM (Stiffness)
    gm = anchor_a / (tokens / 1000)
    
    # Wall-Sided Formula for GZ (Righting Arm)
    bm = gm * 1.5
    theta_rad = math.radians(drift_angle)
    gz = (gm + (0.5 * bm * (math.tan(theta_rad)**2))) * math.sin(theta_rad)
    
    return {
        "RPM": rpm_setting,
        "GZ": round(gz, 4),
        "Status": "STABLE" if gz > 0.05 else "TENDER" if gz > 0 else "CAPSIZED"
    }

# --- THE LIVE TEST DATA (120,000 TOKENS) ---
target_tokens = 120000
test_drift = 25.0  # The 'Dory Effect' Angle

print(f"--- AXIOMLABS LIVE TESTING: THROTTLE SCALING ---")
print(f"Target Displacement: {target_tokens} Tokens\n")

for rpm in [750, 1200, 2500]:
    results = run_throttle_test(target_tokens, rpm, test_drift)
    print(f"[{rpm} RPM] -> GZ: {results['GZ']} | STATUS: {results['Status']}")

print("\nCONCLUSION: At 120k tokens, the 750 RPM Anchor is TENDER.")
print("The 1200 RPM 'High-Tide' Shackle is required for heavy seas.")
