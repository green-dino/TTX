class RiskAssessmentTool:
    def calculate_risk(self, tp, vp, c, i):
        risk = (tp * vp) / (c * i)  # Parentheses added for correct order of operations
        return risk

    def main(self):
        print("Welcome to the Risk Assessment Tool")
        print("Please provide the following information:")
        
        tp = float(input("Threat (t): "))
        vp = float(input("Vulnerability (v): "))
        c = float(input("Countermeasure Effectiveness (c): "))
        i = float(input("Impact (i): "))
        
        risk = self.calculate_risk(tp, vp, c, i)
        
        print(f"Calculated Risk: {risk}")

if __name__ == "__main__":
    risk_tool = RiskAssessmentTool()
    risk_tool.main()
