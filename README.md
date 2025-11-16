# 🔐 Projeto Educacional de Criptografia com Python  

## 🎯 Objetico
Este projeto foi desenvolvido para fins **exclusivamente educacionais**, como parte do Bootcamp  
**Formação Cybersecurity Specialist – DIO**.  

O objetivo é demonstrar, de forma segura, como arquivos podem ser criptografados e recuperados utilizando criptografia simétrica.  
Isso permite compreender conceitos que se assemelham ao funcionamento de ransomwares,  
porém **sem qualquer comportamento malicioso**.

---

## 📂 Estrutura do Projeto
````
projeto-ransomware/
│
├── files/
│   ├── teste1.txt
│   ├── teste2.txt
│   └── qualquer_arquivo.txt
│
├── encrypter.py
├── decrypter.py
└── chave.key
````

## 🧰 Tecnologias Utilizadas

- Python 3
- Biblioteca `cryptography` (Fernet)

Instalação:

```
pip install cryptography
````
## ▶️ Como Executar
1. Crie o arquivo teste.txt:

2. Execute o criptografador:
````
python encrypter.py
````
Resultado:

Arquivo criptografado com sucesso!

3. Execute o descriptografador:
````
python decrypter.py
````
Resultado:

Arquivo descriptografado com sucesso!

## 🧠 O que você aprende neste projeto
* Conceitos fundamentais de criptografia simétrica

* Criação e gerenciamento de chaves

* Integridade dos dados com HMAC

* Base conceitual para entender como ransomwares bloqueiam arquivos

* Boas práticas de segurança e uso ético

## ⚠️ Uso Ético
Este projeto é apenas educacional.

Não deve ser utilizado para:

* ❌ violar privacidade

* ❌ criptografar arquivos de terceiros

* ❌ testar em sistemas que você não possui

* ❌ fins maliciosos ou ilegais

Utilize sempre dentro de ambientes controlados e de estudo.

## Conclusão

Este projeto representa um passo importante na jornada de aplicação prática dos conceitos explorados, reunindo conhecimentos de desenvolvimento, automação e segurança para construir uma 
solução sólida e funcional. A iniciativa não apenas reforça habilidades técnicas, mas também amplia a capacidade de pensar de forma estratégica, estruturada e orientada a 
resultados — um fundamento essencial para qualquer profissional que deseja evoluir na área de tecnologia.

Com isso, o repositório permanece aberto para melhorias, contribuições e novas ideias. A construção contínua é o que transforma projetos em ferramentas valiosas. 
Sinta-se à vontade para sugerir aprimoramentos, relatar problemas ou criar novas features.
