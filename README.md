<p align="center">
<img src="http://mythologian.net/wp-content/uploads/2018/01/Eye-of-Ra-Symbol-and-Its-Meaning.png" width="150" height="150"></img>
</p>

# Anubis

### Abstract

A theoretical quantum resistant pseudonymous peer-to-peer instant messenger, utilising a suite of potential post quantum cryptographic algorithms that makes it infeasable for an adversary with access to a sufficently powerful quantum computer to break. The messenger will employ either Asymmetric or Symmetric quantum resistant encryption methods to encrypt and decrypt messages sent and received, BCrypt for hashing and salts to encrypt user passwords and a modus-operandi on not storing any and all current and historical information on messages sent and received, only a database of pseudonymous users.

### Research

#### Asymmetric Encryption Methods

* Lattice Based Cryptography
* McEliece 

Quantum resistant asymmetric public-key based cryptographic algorithms unrelated to integer factorisation and logarithmic problems will be used to ensure resistance to Shor's algorithm<sup> 1</sup> and Grover's algorithm. The public-key based algorithm used will either be based upon the computational lattice problem<sup> 2</sup> or hardness of decoding a general linear code (McEliece cryptosystem)<sup> 5</sup>, both of which theoretically have the greatest known resistance to an attack by a quantum computer.

#### Symmetric Encryption Methods

For quantum resistant symmetric key based cryptographic algorithms, AES-256 will be used. Though AES-256 has some suceptibility to Grover's quantum search algorithm, a method to theoretically break AES-256 completely (Akin to that of RSA and Shor's algorithm) by a conventional quantum attack has yet to be discovered. Effectively breaking AES-256 through means of a practical attack (non brute force attack) will still require some form of exhaustive keyspace search like what is used today. Examples of which include a Biclique cryptanalysis attack or an implementation of Grover's quantum search algorithm on a Quantum computer.

#### Block Cipher Techniques as outlined by NIST

Block Cipher Confidentiality Modes:

* ECB<sup> 4</sup> (Electronic Codebook)
* CBC<sup> 5</sup> (Cipher Block Chain) - **Depreciated in TLS 1.3 and difficult to implement - Vulnerable to Padding Oracle Attack and Timing Attacks**
* OFB<sup> 6</sup> (Output Feedback)
* CFB<sup> 7</sup> (Cipher FeedBack)
* CTR<sup> 8</sup> (Counter Mode)
* XTS-AES<sup> 9</sup> (XEX-Based Tweaked-Codebook Mode with Ciphertext stealing)
* FF1<sup> 10</sup> (Format-Preserving Feistel-Based Encryption Mode 1)
* FF3<sup> 10</sup> (Format-Preserving Feistel-Based Encryption Mode 1) - **no longer suitable as a general-purpose FPE (Format-preserving encryption) method due to vulnerability - NIST conclusion 12/04/2017**

Block Cipher Combined Modes for Confidentiality and Authentication:

* GCM<sup> 11</sup> (Galois Counter Mode)
* CCM<sup> 12</sup> (Counter with CBC-MAC)
* KW<sup> 13</sup> (Key Wrap)
* KWP<sup> 13</sup> (Key Wrap with Padding)
* TKW<sup> 13</sup> (TDEA Key Wrap)

**Comparison of GCM and CBC**

In CBC blocks of data are encrypted by taking the current plaintext block and applying an XOR (Exclusive-Or) against the previous ciphertext block (or IV). The result of this XOR is sent through the block cipher, where the final output of the block cipher is the ciphertext block. Unlike CBC, GCM provides both privacy (through encryption) and integrity (through authentication). To provide encryption, GCM maintains a counter for each block of data. It sends the current value of the counter through the block cipher and takes the output of the block cipher which it then XOR against the plain text in order to form the ciphertext. Through encryption an authentication tag is produced to verify the integrity of the data. The encrypted text output from GCM contains the IV, ciphertext and authentication produced in parallel, whereas CBC produces only the IV and ciphertext due to its inherent lack of authentication. GCM is considered more versatile than CBC due to it's speed and ability to authenticate and encrypt in parallel.
In terms of the project and as outlined in the above comparison between GCM (Block Cipher with Combined Modes for Confidentiality and Authentication) and CBC (Block Cipher for Confidentiality Modes), block ciphers which combine both confidentiality and authentication will be preferred.

**Comparison of GCM and CCM**

Both GCM AND CCM are block ciphers which combine both confidentiality and authentication, and are considered the de-facto modes of operating the block cipher. Both modes have potential caveats such as GCM is vulnerable to different timing side channel attacks if you cannot guarantee that you are using hardware Galois field arithmetic. CCM on the other hand is slower due to the inherent need of two cipher calls per block instead of field multiplication and a cipher call like GCM. Overall GCM should be considered superior to CCM for most applications that require authenticated encryption due to CCM suceptibility to bit flipping and other attacks that can be mounted against counter or other stream modes. In terms of this project, both GCM and CCM are potential modes to operate the block cipher and are largely similar. Althout some IEEE 802 standards tend to pick CCM over GCM due to HW implementation gate counts, due to the speed differences between GCM and CCM as well as the inherent suceptibilities found in CCM, this project will use GCM as the block cipher mode of operation.

#### Outline of Password Encryption Methods

Hashing Algorithms:

* BCrypt
* PBKDF2 (Password-Based Key Derivation Function 2)
* Argon 2
* SHA-512

**Comparison of BCrypt and PBKDF2**



**Conclusion**
Password encryption will employ methods for both hashing and salting. Hash values will utilise BCrypt password hashing function to reduce the vulnerability of brute force attacks, with a selected key to byte map of 64 and 100 encryption rounds to reduce preimage collision and vulnerability to Grover's algorithm<sup> 14</sup>. The hashing algorithm used will be BCrypt's implementation in Python. The use of BCrypt is due to it theoretically not being weakened by Grover's algorithm<sup> 15</sup>.
Salt values will be generated randomly through BCrypt, utilising 20 rounds to ensure a higher level entropy between generated salt values.

### References

<sup>1 </sup>https://arxiv.org/abs/quant-ph/9508027

<sup>2 </sup>https://en.wikipedia.org/wiki/Lattice_problem#Use_in_cryptography

<sup>3 </sup>https://en.wikipedia.org/wiki/McEliece_cryptosystem

<sup>4 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB)

<sup>5 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_(CBC)

<sup>6 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_Feedback_(OFB)

<sup>7 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#CFB

<sup>8 </sup>https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)

<sup>9 </sup>https://en.wikipedia.org/wiki/Disk_encryption_theory#XEX-based_tweaked-codebook_mode_with_ciphertext_stealing_(XTS)

<sup>10 </sup>https://en.wikipedia.org/wiki/Format-preserving_encryption#Acceptance_of_FPE_algorithms_by_standards_authorities

<sup>11 </sup>https://en.wikipedia.org/wiki/Galois/Counter_Mode

<sup>12 </sup>https://en.wikipedia.org/wiki/CCM_mode

<sup>13 </sup>https://en.wikipedia.org/wiki/Key_Wrap

<sup>14 </sup>https://en.wikipedia.org/wiki/Grover%27s_algorithm

<sup>15 </sup>https://cs.stackexchange.com/questions/586/could-quantum-computing-eventually-be-used-to-make-modern-day-hashing-trivial-to

<sup>15 </sup>https://stackoverflow.com/questions/2768807/quantum-computing-and-encryption-breaking

**Supplimentary References**

* Title: Lattice-Based Cryptography: A Practical Implementation, Author: Michael Rose - https://www.uow.edu.au/~thomaspl/pdf/Rose11.pdf

