# elliptic-curve-cryptography
This is a repository to experiment with different protocols for key exchange and message encryption using elliptic curves. I will be using my elliptic-curves-over-finite-fields and attacks-on-the-discrete-log-problem in the processof encrypting and decrypting messages and breaking these systems by solvin the DLP for small example fields.

Current goals:

* Implement and break the Diffie-Hellman key exchange.
* Implement and break Massey-Omura.
* Implement and break ElGamal public key.

I will add more as I continue to learn about elliptic curve cryptography. Eventually I want to roll and break my own cryptosystems; this will be pursued in another repository as a separate project using knowledge gained while working in this repository.

Note: this only works for prime fields for now as I'm still learning how to implement elements of Fq in general using Python. I may or may not return to this in the future, but for now it represents a "proof of concept" of an implementation of elliptic curves over finite fields.
