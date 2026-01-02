#### Title : 
[When TLS Meets Proxy on Mobile](https://link.springer.com/chapter/10.1007/978-3-030-57878-7_19)
##### Authors : 
Joyanta Debnath (The University of Iowa), Sze Yiu Chau (The Chinese University of Hong Kong,), and Omar Chowdhury (The University of Iowa)
##### Conference : 
18th International Conference on Applied Cryptography and Network Security (ACNS 2020)

##### Summary : 
Increasingly more mobile browsers are developed to use proxies for traffic compression and censorship circumvention. While these browsers can offer such desirable features, their security implications are, however, not well understood, especially when tangled with TLS. Apart from vendor-specific proprietary designs, there are mainly 2 models of using proxies with browsers: TLS interception and HTTP tunneling. To understand the current practices employed by proxy-based mobile browsers, we analyze 34 Android browser apps that are representative of the ecosystem, and examine how their deployments are affecting communication security. Though the impacts of TLS interception on security was studied before in other contexts, proxy-based mobile browsers were not considered previously. In addition, the tunneling model requires the browser itself to enforce certain desired security policies (e.g., validating certificates and avoiding the use of weak cipher suites), and it is preferable to have such enforcement matching the security level of conventional desktop browsers. Our evaluation shows that many proxy-based mobile browsers downgrade the overall quality of TLS sessions, by for example allowing old versions of TLS (e.g., SSLv3.0 and TLSv1.0) and accepting weak cryptographic algorithms (e.g., 3DES and RC4) as well as unsatisfactory certificates (e.g., revoked or signed by untrusted CAs), thus exposing their users to potential security and privacy threats.

##### Link to Experiments:
[Google Drive Link](https://drive.google.com/file/d/1v8cPBEGRJlyyv_1Y0D8MnYVJCdR5-5u_/view?usp=sharing)

#### Citation:
Please, use the following *bibtex* for citing this work.

```
@InProceedings{10.1007/978-3-030-57878-7_19,
author="Debnath, Joyanta
and Chau, Sze Yiu
and Chowdhury, Omar",
editor="Conti, Mauro
and Zhou, Jianying
and Casalicchio, Emiliano
and Spognardi, Angelo",
title="When TLS Meets Proxy on Mobile",
booktitle="Applied Cryptography and Network Security",
year="2020",
publisher="Springer International Publishing",
address="Cham",
pages="387--407",
isbn="978-3-030-57878-7"
}
```

#### Contributors:
Please, feel free to contact one of us if you have any questions.
* [Joyanta Debnath](https://joyantadebnath.github.io/homepage/)
* [Omar Chowdhury](https://www3.cs.stonybrook.edu/~omar/)
* [Sze Yiu Chau](https://szeyiuchau.github.io/)
