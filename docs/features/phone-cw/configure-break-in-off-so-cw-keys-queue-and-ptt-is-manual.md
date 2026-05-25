# Configura e desativa a operação Break-in para que as teclas CW sejam enfileiradas e o PTT seja manual

Quando o Breakin está DESLIGADO, os eventos de tecla CW do teclado e MIDI são enfileirados e enviados ao rádio sem acionar automaticamente a transmissão (TX). Você aciona o PTT manualmente para começar a transmitir. Use esta configuração quando quiser controle total sobre quando o transmissor chaveia — por exemplo, durante operações de concurso ou ao usar um amplificador linear que precisa de sequenciamento deliberado do PTT.

## Antes de começar

- Conecte-se a um rádio FLEX-8600. O applet Phone/CW requer uma conexão ativa com o rádio.
- Defina o slice ativo para um modo CW para que o applet mude para o painel CW. O controle Breakin só é visível no subpainel CW.

## Passos

1. Abra o applet Phone/CW. Clique no botão **P/CW** na barra lateral direita ou confirme que ele já está visível no Painel de Applets.
2. Verifique se o subpainel CW está sendo exibido. Se o painel Phone for exibido, altere o modo do slice ativo para CW no rádio.
3. Localize o botão de alternância **Breakin** no subpainel CW.
4. Se **Breakin** estiver aceso (ativo), clique para desativá-lo. O botão aparecerá apagado quando o break-in estiver desabilitado.
5. Chaveie CW usando seu teclado ou controlador MIDI. Os caracteres são enfileirados e enviados ao rádio, mas o rádio não ativa TX automaticamente.
6. Pressione PTT manualmente para chavear o transmissor antes ou enquanto o keyer envia os caracteres enfileirados.

## O que cada controle faz

| Controle            | Comportamento                                                                                                                                                                                                                                                                                   | Padrão                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Breakin**         | Alterna entre full break-in (QSK). Quando LIGADO, as bordas das teclas disparam TX e o atraso de break-in mantém o relé aberto entre caracteres. Quando DESLIGADO, os caracteres chaveados são enfileirados e o PTT deve ser engajado manualmente.                                                | —                                                        |
| **Delay (CW)**      | Define o tempo de espera (hang time) do break-in CW — quanto tempo o relé permanece chaveado após o último elemento. Relevante quando Breakin está LIGADO. O slider ajusta de 0 a 2000 ms em passos de 10 ms. Na v0.9.8, você pode clicar no QLineEdit adjacente e digitar um valor diretamente (0–2000). | 500 ms                                                   |
| **Speed (CW)**      | Define a velocidade de chaveamento CW em palavras por minuto. O slider ajusta de 5 a 100 WPM. Na v0.9.8, você pode clicar no QLineEdit adjacente e digitar um valor diretamente (5–100).                                                                                                            | 20 WPM                                                   |
| **Sidetone**        | Alterna o monitor de sidetone CW. Controla tanto o monitor alimentado por DAX do rádio quanto o CwSidetoneGenerator local de baixa latência em conjunto. O tom e o pan seguem automaticamente as configurações `cw_pitch` e `mon_pan_cw` do rádio. Na v26.5.3, o sidetone CW é roteado para a saída de áudio selecionada pelo usuário em vez da saída padrão (#2899). | —                                                        |
| **Sidetone volume** | Define o volume do monitor CW. Controla tanto o volume do lado do rádio (`mon_gain_cw`) quanto o volume do gerador de sidetone local em conjunto. O slider ajusta de 0 a 100. Na v0.9.8, você pode clicar no QLineEdit adjacente e digitar um valor diretamente (0–100).                             | 50                                                       |
| **L / R pan (CW)**  | Define o pan estéreo do monitor CW. Chama `TransmitModel::setMonPanCw` e aplica pan de potência constante ao gerador de sidetone local. Clique duas vezes para centralizar em 50 (centro).                                                                                                       | 50                                                       |
| **Iambic**          | Alterna o keyer de paddle iâmbico.                                                                                                                                                                                                                                                              | —                                                        |
| **Pitch < / >**     | Define o tom do sidetone CW. Clique nos botões **<** ou **>** para aumentar/diminuir em passos de 10 Hz, ou clique no QLineEdit e digite um valor diretamente (100–6000 Hz). Chama `TransmitModel::setCwPitch`. Na v0.9.8, o QLineEdit aceita entrada direta digitada.                            | 600 Hz                                                   |
| ALC (no painel Phone) | Mostra a leitura do controle automático de nível (ALC) do MeterModel::swAlcChanged (pico SSB pós-ALC de software em dBFS). Preenche da direita para a esquerda: vazio em -20 dBFS, cheio em 0 dBFS. Na v26.5.3, o medidor ALC é inicializado imediatamente para -20 dBFS no início. | Alterado de HWALC (tensão RCA) para SW ALC meter na v26.5.1 (#2552). Espelhado por um medidor idêntico no subpainel CW. |
| ALC (no painel CW)  | Espelha o medidor ALC do painel Phone; ambos leem de MeterModel::swAlcChanged para leituras consistentes entre voz e CW. Na v26.5.3, o medidor ALC é inicializado imediatamente para -20 dBFS no início. | Adicionado na v26.5.1 (#2552) como parte da divisão do SW ALC meter. Usa o modo HGauge::setFillFromRight.               |
| **Compression**     | Mostra a quantidade de compressão de fala em dB por meio da leitura COMPPEAK do MeterModel. Na v26.5.3, a compressão é exibida como um valor positivo de 0 a 25 dB (0 = sem compressão, 25 = compressão total), invertido para -25 a 0 dB na face do medidor. | —                                                        |
| **Level**           | Mostra o nível de pico do microfone em dBFS. Na v26.5.3, o nível do microfone é suprimido durante a recepção quando a opção "Medidor de nível durante recepção" está desativada, independentemente da fonte do microfone. | —                                                        |

## Dicas

- Com Breakin DESLIGADO, nenhum envelope de PTT automático é aplicado. O rádio não transmitirá caracteres enfileirados até que você acione o PTT. Solte o PTT após o último caractere ser enviado para retornar ao RX.
- Se você estiver usando um amplificador externo, Breakin DESLIGADO lhe dá tempo para fechar o relé T/R do amplificador antes do keyer começar a enviar.
- Para ajustar quanto tempo o relé permanece engajado entre caracteres quando você posteriormente ligar Breakin novamente, use o slider **Delay (CW)** (0–2000 ms) ou digite um valor no QLineEdit adjacente.
- Na v26.5.3, o sidetone CW é automaticamente roteado para o dispositivo de saída de áudio selecionado nas configurações de Áudio do AetherSDR, não mais para a saída padrão do sistema. Verifique sua seleção de saída de áudio se não ouvir sidetone.

## Solução de problemas

- **O rádio transmite imediatamente quando uma tecla é pressionada, mesmo com Breakin aparentemente desligado** — Este era um problema conhecido em versões anteriores à v0.9.7, onde um envelope de PTT automático sobrepunha a configuração Breakin. Confirme se o AetherSDR está na v0.9.7 ou posterior.
- **O painel CW não está visível; os controles Phone são mostrados** — O applet muda para o subpainel CW automaticamente apenas quando o slice ativo está em um modo CW. Altere o modo do slice para CW no rádio.
- **O slider Delay volta após digitar um valor** — Isso foi corrigido na v0.9.8 (#2428). O valor agora é armazenado em cache imediatamente para que a emissão do rádio não force o slider de volta.
- **O medidor ALC mostra uma leitura congelada** — Na v26.5.3, o medidor ALC é inicializado para -20 dBFS na construção. Se a leitura permanecer em -20 dBFS, verifique se o rádio está transmitindo e se há um sinal de áudio presente.
- **O medidor de nível do microfone mostra -150 dBFS durante a recepção** — Na v26.5.3, o medidor de nível é suprimido durante a recepção quando a opção "Medidor de nível durante recepção" está desativada nas configurações do TransmitModel. Para ver o nível do microfone durante a recepção, ative essa opção.
- **Não ouço sidetone CW** — Na v26.5.3, verifique se a saída de áudio correta está selecionada nas configurações de Áudio do AetherSDR. O sidetone agora roteia para a saída de áudio do usuário, não para a saída padrão do sistema (#2899).

## Relacionados

- [Ajustar o atraso de break-in CW](set-cw-break-in-delay.md)
- [Usar teclado ou MIDI para acionar chave direta ou pás iâmbicas](use-keyboard-or-midi-to-trigger-straight-key-or-iambic-paddles.md)
- [Habilitar chaveamento iâmbico de paddle](enable-iambic-paddle-keying.md)
- [Definir velocidade de chaveamento CW em WPM](set-cw-keying-speed-in-wpm.md)
- Ver controles do applet Phone/CW