---
marp: true 
theme: uncover

---
## Data Leak Incident Summary

### What Happened?
In this data leak incident, cybercriminals used a method called "credential stuffing" to exploit reused passwords from previous breaches. These attackers obtained passwords from other breaches and attempted to use them to gain unauthorized access to 23andMe user accounts. Most users tend to reuse passwords across multiple online platforms, making it easier for attackers to compromise accounts. The attackers leveraged an opt-in feature known as "DNA Relatives" to access genetic data of similar groups. Notably, 23andMe itself was not directly hacked; rather, the breach was facilitated by the reuse of previously breached passwords by 23andMe users, resulting in the theft of sensitive genetic data.
---
### Proactive Measures for Organizations
To prevent similar intrusions, organizations can take the following proactive steps:

1. **Integrate with haveibeenpwned.com**: Companies can integrate with haveibeenpwned.com to alert users if their passwords have been compromised and are available online due to previous breaches. This helps discourage users from reusing passwords on their websites, enhancing security and preventing account takeovers.

2. **Implement Multi-Factor Authentication (MFA)**: Make MFA readily available to users and emphasize its importance. A lack of MFA should be as conspicuous as driving without a seatbelt. Users should be encouraged to enable MFA, which can significantly enhance account security.
---
### Individual Risk Mitigation

#### Individuals can take the following steps to limit their risk of account takeover on websites:

1. **Avoid Password Reuse**: Refrain from reusing passwords and instead use long, random, and unique passwords for each website. Consider generating and storing these passwords with a password manager, or use passkeys where available to eliminate the need for passwords.

2. **Use Appropriate MFA**: Employ the right form of multi-factor authentication based on your threat model and digital literacy. For many, app-based MFA is a minimum requirement, and even SMS-based 2FA is better than no additional authentication for protection against credential stuffing attacks. FIDO solutions, such as Yubico YubiKeys, are effective for many users.

3. **Sign Up for haveibeenpwned.com Alerts**: Register for alerts from haveibeenpwned.com to receive notifications if your usernames, email addresses, or passwords are compromised in a breach. In such cases, change the affected passwords immediately and ensure that MFA is enabled for those accounts.
---
