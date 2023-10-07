import pandas as pd

mitre_process = {
    'A(ATT&CK Tactics)': ['B(Initial Access)', 'C(Execution)', 'D(Persistence)', 'E(Privilege Escalation)', 
                          'F(Defense Evasion)', 'G(Credential Access)', 'H(Discovery)', 'I(Lateral Movement)', 
                          'J(Collection)', 'K(Exfiltration)', 'L(Impact)'],
    'B(Initial Access)': ['B1(External Remote Services)', 'B2(Phishing)', 'B3(Hardware Additions)', 
                          'B4(Taint Shared Content)'],
    'C(Execution)': ['C1(Command and Scripting Interpreter)', 'C2(Executable Installer)', 'C3(Rootkit)', 
                     'C4(Taint Shared Content)'],
    'D(Persistence)': ['D1(Boot or Logon Autostart Execution)', 'D2(Service Registry Permissions Weakness)', 
                      'D3(Scheduled Task/Job)', 'D4(Startup Items)', 'D5(Taint Shared Content)'],
    'E(Privilege Escalation)': ['E1(Permission Groups Discovery)', 'E2(Taint Shared Content)'],
    'F(Defense Evasion)': ['F1(Indicator Removal on Host)', 'F2(Process Injection)', 'F3(Runtime Data Manipulation)', 
                           'F4(Software Packing)', 'F5(Taint Shared Content)'],
    'G(Credential Access)': ['G1(Account Manipulation)', 'G2(Credential Dumping)', 'G3(Password Cracking)', 
                            'G4(Taint Shared Content)'],
    'H(Discovery)': ['H1(Account Discovery)', 'H2(Network Service Scanning)', 'H3(Network Share Discovery)', 
                    'H4(System Network Configuration Discovery)', 'H5(Taint Shared Content)'],
    'I(Lateral Movement)': ['I1(Exploitation for Client Execution)', 'I2(Lateral Tool Transfer)', 
                            'I3(Remote Desktop Protocol)', 'I4(Taint Shared Content)'],
    'J(Collection)': ['J1(Data from Information Repositories)', 'J2(Data from Local System)', 'J3(Data Staged)', 
                      'J4(Email Collection)', 'J5(Screen Capture)', 'J6(Taint Shared Content)'],
    'K(Exfiltration)': ['K1(Data Transfer Size Limits)', 'K2(Exfiltration Over C2 Channel)', 
                        'K3(Exfiltration Over Other Network Medium)', 'K4(Exfiltration Over Physical Medium)', 
                        'K5(Taint Shared Content)'],
    'L(Impact)': ['L1(Data Destruction)', 'L2(Disk Structure Wipe)', 'L3(Endpoint Denial of Service)', 
                  'L4(Network Denial of Service)', 'L5(Service Stop)', 'L6(Taint Shared Content)'],
}

df = pd.DataFrame(data)
