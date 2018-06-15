# Anubis
A post quantum resistant peer-to-peer instant messenger utilising end-to-end encryption (E2EE) on messages sent and received.

**Encryption methods to maximise resistance to quantum based attacks:**

#*Password generation*
Hash values utilise PBKDF2 (Password-Based Key Derivation Function 2) to reduce vulnerability to brute force attacks, with a selected key to byte map of 128 and 16 encryption rounds to reduce vulnerability to Grover's algorithm. Although BCrypt is theortically not weakened by Grover's algorithm, this added layer of vulnerability reduction is simply a precaution.

BCrypt Salt values are generated randomly through BCrypt utilising 20 rounds ensure a higher level randomness between generated salt values.
