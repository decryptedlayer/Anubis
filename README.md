

# Anubis
<p align="left">
<img src="https://www.shareicon.net/data/256x256/2016/03/20/737028_shapes_512x512.png" width="50" height="50"></img>
</p> 

**Abstract**

A theoretical quantum resistant peer-to-peer instant messenger utilising a suite of potential post quantum cryptographic algorithms, that makes it infeasable for an adversary with access to a sufficently powerful quantum computer to break.

**Encryption methods to maximise and ensure theoretical resistance to quantum based attacks**

* Password encryption (Hashing and salting methods):
Hash values utilise PBKDF2 (Password-Based Key Derivation Function 2) to reduce vulnerability to brute force attacks, with a selected key to byte map of 64 and 100 encryption rounds to reduce preimage collision and vulnerability to Grover's algorithm<sup> 1</sup>. Although BCrypt is theoretically not weakened by Grover's algorithm<sup> 2</sup>, this added layer of vulnerability reduction is simply a precaution. Salt values are generated randomly through BCrypt, utilising 20 rounds to ensure a higher level entropy between generated salt values.
* Message encryption and verification (E2EE and signature methods):
Messages will either be encrypted asymmetrically end to end, with only the ciphertext sent through the clear, or will be encrypted and signed symmetrically with a shared private session key that can be accessed on an encrypted centralised server for message encryption and decryption.

**Asymmetric Encryption Methods**

Quantum resistant asymmetric public-key based cryptographic algorithms unrelated to integer factorisation and logarithmic problems will be used to ensure resistance to Shor's algorithm<sup> 3</sup> and Grover's algorithm. The public-key based algorithm used will either be based upon the computational lattice problem<sup> 4</sup> or hardness of decoding a general linear code (McEliece cryptosystem)<sup> 5</sup>, both of which theoretically have the greatest known resistance to an attack by a quantum computer.

**Symmetric Encryption Methods**

For quantum resistant symmetric key based cryptographic algorithms, AES-256 will be used. Though AES-256 has some suceptibility to Grover's quantum search algorithm, a method to theoretically break AES-256 completely (Akin to that of RSA and Shor's algorithm) by a conventional quantum attack has yet to be discovered. Effectively breaking AES-256 through means of a practical attack (non brute force attack) will still require some form of exhaustive keyspace search like what is used today. Examples of which include a Biclique cryptanalysis attack or an implementation of Grover's quantum search algorithm on a Quantum computer.

**Block Cipher modes of operation**

Common block cipher modes of operation include: 

* GCM<sup> 6</sup> (Galois Counter Mode)
* CBC<sup> 7</sup>(Cipher Block Chain)
* CFB<sup> 8</sup>(Cipher Feed Back)
* CTR<sup> 9</sup>(Counter Mode)


The AES encryption mode which will be implemented is GCM. In CBC blocks of data are encrypted by taking the current plaintext block and applying an XOR (Exclusive-Or) against the previous ciphertext block (or IV). The result of this XOR is sent through the block cipher, where the final output of the block cipher is the ciphertext block. Unlike CBC, GCM provides both privacy (through encryption) and integrity (through authentication). To provide encryption, GCM maintains a counter for each block of data. It sends the current value of the counter through the block cipher and takes the output of the block cipher which it then XOR against the plain text in order to form the ciphertext. Through encryption an authentication tag is produced to verify the integrity of the data. The encrypted text output from GCM contains the IV, ciphertext and authentication produced in parallel, whereas CBC produces only the IV and ciphertext due to its inherent lack of authentication. GCM is considered more versatile than CBC due to it's speed and ability to authenticate and encrypt in parallel.

**Message Authentication Methods**

To ensure integrity and authenticity of each message sent and received, Poly1305-AES<sup> 10</sup> will be used. Poly1305-AES which is a cryptographic message authentication code (MAC)<sup>11 </sup>, utilises the AES block cipher to expand its keyspace ontop of a 128-bit (16 byte) computed authenticator of a variable-length message. The security of Poly1305-AES is nearly identical to the underlying AES block cipher algorithm. Consequently, the only way for a quantum computer to attack Poly1305-AES is by using Grover's quantum search algorithm which will still take an exponential amount of time to break.

  **Client Authentication Methods**

* Authentication Server:
In order to authenticate users, Anubis uses a seperate authentication server for verification purposes which acts similar in respects to Kerberos used in Windows. When a user successfully logs into Anubis they are assigned a TGT (Ticket Granting Ticket) which is a small encrypted identification file with a limited validity period. The TGT file contains a session key, expiration date, and user IP address in order to protect against main-in-the-middle attacks. A database linked to the Authentication server will constantly update with the reissue of TGT assigned to users allowing for a constant and up to data source of all users online and their associated IP addresses for communication. The authentication server also processes whether one user is authorised to message another, this is dependant if the two users are connected or not.

## Todo

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## References

<sup>1 </sup>https://en.wikipedia.org/wiki/Grover%27s_algorithm

<sup>2 </sup>https://cs.stackexchange.com/questions/586/could-quantum-computing-eventually-be-used-to-make-modern-day-hashing-trivial-to

<sup>2 </sup>https://stackoverflow.com/questions/2768807/quantum-computing-and-encryption-breaking

<sup>3 </sup>https://arxiv.org/abs/quant-ph/9508027

<sup>4 </sup>https://en.wikipedia.org/wiki/Lattice_problem#Use_in_cryptography

<sup>5 </sup>https://en.wikipedia.org/wiki/McEliece_cryptosystem

<sup>6 </sup>https://en.wikipedia.org/wiki/Galois/Counter_Mode

<sup>7 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_(CBC)

<sup>8 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CFB

<sup>9 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)

<sup>10 </sup>https://en.wikipedia.org/wiki/Poly1305#Security

<sup>11 </sup>https://en.wikipedia.org/wiki/Message_authentication_code

**Supplimentary References**

* Title: Lattice-Based Cryptography: A Practical Implementation, Author: Michael Rose - https://www.uow.edu.au/~thomaspl/pdf/Rose11.pdf

