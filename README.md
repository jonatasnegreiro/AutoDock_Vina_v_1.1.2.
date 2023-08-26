# Pipeline para Simulações de Docking Molecular com AutoDock Vina versão 1.1.2.

Este pipeline foi criado para facilitar a realização de simulações de docking molecular utilizando o AutoDock Vina versão 1.1.2. Embora as técnicas de docking molecular possam ser simples de executar, uma preparação prévia dos arquivos é necessária para garantir a acurácia dos resultados. Este pipeline visa simplificar essa etapa.

## Como funciona

Com este pipeline, o usuário pode escolher uma proteína disponível no Protein Data Bank (PDB), tratá-la para eliminar resíduos não proteicos e protonar a proteína utilizando o servidor da web PDB2PQR. O pipeline gera os arquivos necessários para a simulação, incluindo o arquivo conf.txt, que contém as coordenadas do ligante co-cristalizado e servirá como base para as próximas simulações. Ele também gera os arquivos receptor.pdbqt e ligante.pdbqt.

Uma vez que todos os arquivos necessários estão prontos, o usuário pode realizar a simulação e calcular o RMSD da etapa de redocking molecular para confirmar se as condições de simulação estão adequadas.

## Uso

O pipeline é executado de maneira intuitiva e o usuário deve seguir a sequência fornecida. Ao final da simulação, todos os arquivos podem ser salvos no Google Drive do usuário para referência futura.

## Suporte

Se você encontrar algum erro no código, não hesite em entrar em contato pelo e-mail: jonatasmartinsif@gmail.com

---
