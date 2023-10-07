import pandas as pd

class RiskAssessmentTool:

    def calculate_risk(self, tp, vp, c, i):
        risk = (tp * vp) / (c * i)
        return risk

    def main(self):
        print("Welcome to the Risk Assessment Tool")
        print("Please provide the following information:")        
        tp = float(input("Threat (t): "))
        vp = float(input("Vulnerability (v): "))
        c = float(input("Countermeasure Effectiveness (c): "))
        i = float(input("Impact (i): "))       
        risk = self.calculate_risk(tp, vp, c, i)

        # Create a DataFrame to display the result
        data = {'Threat (t)': [tp], 'Vulnerability (v)': [vp], 'Countermeasure Effectiveness (c)': [c], 'Impact (i)': [i], 'Calculated Risk': [risk]}
        rat_df = pd.DataFrame(data)
        
        print("\nRisk Assessment Results:")
        print(rat_df)

if __name__ == "__main__":
    risk_tool = RiskAssessmentTool()
    risk_tool.main()
