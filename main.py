from optimizer import PyFabEngine

def run_simulation():
    print("--- PyFab-Optimizer v1.0 ---")
    [span_13](start_span)print("Developed by: MFZTX899[span_13](end_span)")
    
    # Simulate a standard wood sheet (e.g., 2440mm x 1220mm)
    engine = PyFabEngine(stock_area=2976800)
    
    # [span_14](start_span)Mock data representing a parsed design from ArtCAM[span_14](end_span)
    design_area = 2650000 
    
    result = engine.calculate_efficiency(design_area)
    
    print(f"Current Material Efficiency: {result}%")
    if result > 85:
        [span_15](start_span)print("Status: High Efficiency - Waste reduction targets met[span_15](end_span).")
    else:
        print("Status: Optimization Recommended.")

if __name__ == "__main__":
    run_simulation()
  
