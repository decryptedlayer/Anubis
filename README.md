<p align="center">
<a style="pointer-events: none; cursor: default;">
<img src="https://www.shareicon.net/data/256x256/2016/03/20/737028_shapes_512x512.png" width="150" height="150"></img>
</a>
</p>

# Anubis 

**Abstract**

A theoretical quantum resistant peer-to-peer instant messenger utilising a suite of potential post quantum cryptographic algorithms, that makes it infeasable for an adversary with access to a sufficently powerful quantum computer to break.

**Encryption methods to maximise and ensure theoretical resistance to quantum based attacks**

* Password encryption (Hashing and salting methods):
Hash values utilise PBKDF2 (Password-Based Key Derivation Function 2) to reduce vulnerability to brute force attacks, with a selected key to byte map of 64 and 100 encryption rounds to reduce preimage collision and vulnerability to Grover's algorithm<sup> 1</sup>. Although BCrypt is theortically not weakened by Grover's algorithm<sup> 2</sup>, this added layer of vulnerability reduction is simply a precaution. Salt values are generated randomly through BCrypt, utilising 20 rounds ensure a higher level entropy between generated salt values.
* Message encryption and verification (E2EE and signature methods):
Messages will either be encrypted asymmetrically end to end, with only the ciphertext sent through the clear, or will be encrypted and signed symmetrically with a shared private session key that can be accessed on an encrypted centralised server for message encryption and decryption.

For quantum resistant asymmetric public-key based cryptographic algorithms unrelated to integer factorisation and logarithmic problems will be used to ensure resistance to Shor's algorithm<sup> 3</sup> and Grover's algorithm. The public-key based algorithm used will either be based upon the the computational lattice problem<sup> 4</sup> or hardness of decoding a general linear code (McEliece cryptosystem)<sup> 5</sup>.

For quantum resistant symmetric key based cryptographic algorithms, AES-256 will be used. Though AES-256 is suceptible to Grover's quantum search algorithm, its ability to be theoretically broken by a conventional quantum attack is unknown. Though strength of AES-256 will be diminished, effectively breaking AES-256 through a practical attack (non brute force attack) means will still require some form of exhaustive keyspace seach such as Biclique cryptanalysis attack or Grover's quantum search algorithm.

To ensure integrity and authenticity of each message sent and received, Poly1305-AES<sup> 6</sup> will be used. Poly1305-AES which is a cryptographic message authentication code (MAC)<sup>7 </sup>, utilises the AES block cipher to expand its keyspace ontop of a 128-bit (16 byte) computed authenticator of a variable-length message. The security of Poly1305-AES is nearly identical to the underlying AES block cipher algorithm. Consequently, the only way for a quantum computer to attack Poly1305-AES is by using Grover's algorithm which will .

**How clients are authenticated and messages sent and received**

* Authentication Server:
In order to authenticate users, Anubis uses a seperate authentication server for verification purposes which acts similar in respects to Kerberos used in Windows. When a user successfully logs into Anubis they are assigned a TGT (Ticket Granting Ticket) which is a small encrypted identification file with a limited validity period. The TGT file contains a session key, expiration date, and user IP address in order to protect against main-in-the-middle attacks. A database linked to the Authentication server will constantly update with the reissue of TGT assigned to users allowing for a constant and up to data source of all users online and their associated IP addresses for communication. The authentication server also processes whether one user is authorised to message another, this is dependant if the two users are connected or not.

**References**

<sup>1 </sup>https://en.wikipedia.org/wiki/Grover%27s_algorithm

<sup>2 </sup>https://cs.stackexchange.com/questions/586/could-quantum-computing-eventually-be-used-to-make-modern-day-hashing-trivial-to

<sup>2 </sup>https://stackoverflow.com/questions/2768807/quantum-computing-and-encryption-breaking

<sup>3 </sup>https://arxiv.org/abs/quant-ph/9508027

<sup>4 </sup>https://en.wikipedia.org/wiki/Lattice_problem#Use_in_cryptography

<sup>5 </sup>https://en.wikipedia.org/wiki/McEliece_cryptosystem

<sup>6 </sup>https://en.wikipedia.org/wiki/Poly1305#Security

<sup>7 </sup>https://en.wikipedia.org/wiki/Message_authentication_code

**Supplimentary References**

* Title: Lattice-Based Cryptography: A Practical Implementation, Author: Michael Rose - https://www.uow.edu.au/~thomaspl/pdf/Rose11.pdf

