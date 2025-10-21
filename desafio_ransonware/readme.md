# Desafio Ransonware (modelo didático)

AVISO IMPORTANTE
----------------
Este repositório contém um modelo didático que implementa um processo de cifragem (encryptor) e decifragem (decryptor) de arquivos. Ele foi desenvolvido exclusivamente para fins educacionais e de pesquisa em cibersegurança. NÃO execute este código em sistemas ou pastas que contenham dados reais ou importantes. A execução inadvertida pode causar perda irreversível de dados.

Você é o único responsável por garantir que o ambiente onde executar este projeto é seguro, isolado e descartável (por exemplo: máquina virtual dedicada, container limpo, snapshot disponível).

Descrição
---------
O projeto demonstra o fluxo conceitual de um ataque de cifragem e sua reversão, dividido em duas partes principais:

- Encryptor: percorre uma pasta de teste (por padrão: `testefiles`), aplica um processo de cifragem nos arquivos dessa pasta e gera os dados necessários para decifrar (por exemplo: chave/metadata). Como parte do exemplo didático, os dados para recuperação são enviados por e-mail (ou simulados) para demonstrar o fluxo de exfiltração da chave.
- Decryptor: recebe a chave de decifração (informada como argumento) e aplica o processo inverso, restaurando os arquivos cifrados na pasta de testes.

Objetivo pedagógico
-------------------
- Entender o fluxo de cifragem/decifragem e os riscos associados.
- Aprender práticas seguras para análise e mitigação de ameaças que envolvem ransomware.
- Demonstrar controles de segurança, backup e resposta a incidentes em ambiente controlado.

Como funciona (visão geral, sem instruções operacionais detalhadas)
------------------------------------------------------------------
- O encryptor identifica arquivos na pasta de testes e aplica um algoritmo de cifragem (ex.: cifra simétrica com chave gerada).
- Os artefatos necessários para a recuperação (por exemplo: chave, parâmetros) são armazenados em um local seguro/externo ou enviados para uma conta de e-mail configurada apenas para demonstração.
- O decryptor aceita a chave correta e reverte o processo, restaurando os arquivos originais.

IMPORTANTE: Este README descreve o comportamento em alto nível — NÃO inclui passos operacionais detalhados que possam ser usados para fins maliciosos.

Recomendações de segurança antes de executar (checklist)
-------------------------------------------------------
- Execute somente em um ambiente isolado e descartável:
  - Máquina virtual (VM) dedicada ou container recém-criado.
  - Desconectar redes não necessárias; preferir rede isolada somente se necessário.
  - Criar um snapshot ou backup da VM antes de qualquer execução.
- Nunca aponte a pasta de testes para diretórios do sistema ou para pastas com dados pessoais/produção.
- Trabalhe apenas com cópias de arquivos pequenos e não sensíveis.
- Revise o código fonte antes de executar: verifique como a chave é gerada, armazenada e transmitida.
- Conceda permissões mínimas ao processo (não execute como root/administrador).
- Tenha um plano para restaurar a máquina (usar o snapshot) se necessário.
- Se desejar, adicione um "modo simulação" (dry-run) que não modifica arquivos — fortemente recomendado para testes iniciais.

Boas práticas pedagógicas
-------------------------
- Explique as implicações éticas e legais antes de demonstrar.
- Mostre técnicas de prevenção e mitigação (backups, segmentação, detecção).
- Demonstre o processo em conjunto com ferramentas de monitoramento (logs, rede) para evidenciar sinais de comprometimento.

Estrutura do repositório (exemplo)
----------------------------------
- desafio_sansonware/
  - encryptor/        (código do encryptor — revisar antes de rodar)
  - decryptor/        (código do decryptor — revisar antes de rodar)
  - testefiles/       (pasta de arquivos de exemplo; manter apenas arquivos de teste)
  - docs/             (documentação adicional, análises e notas didáticas)
  - README.md         (este arquivo)

Aviso legal e ético
-------------------
Este material é fornecido exclusivamente para fins educativos. O uso deste código fora de um ambiente controlado, ou para comprometer sistemas de terceiros, é ilegal e antiético. O autor se exime de qualquer responsabilidade por uso indevido do conteúdo.

Contribuições e melhorias
-------------------------
Contribuições que reforcem a segurança do material são bem-vindas:
- Adicionar um modo "simulação" (dry-run) que não altera arquivos.
- Incluir testes automatizados que validem as operações em ambientes simulados.
- Documentação passo a passo sobre como avaliar impactos e aplicar contramedidas (sempre em contexto controlado).

Contato
-------
Para dúvidas sobre o material didático, segurança e execução controlada, entre em contato com o mantenedor do repositório.
