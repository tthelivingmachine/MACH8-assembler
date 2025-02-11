    ldi r1  255      ; Load 255 (0xFF) into r1
    ldi r2  0x80     ; Load 128 (0x80) into r2
    ldi r3  0x00     ; Load 0 into r3

    ; Test ADD (Unsigned Carry + Overflow)
    alu add r4 r1 r2  ; r4 = r1 + r2 (255 + 128 = 383)
    store r4 r2 r3 0x01   ; Store result for inspection

    ; Test SUB (Zero and Negative)
    alu sub r5 r1 r1  ; r5 = r1 - r1 (255 - 255 = 0)
    store r5 r2 r3 0x02   ; Store result for inspection

    alu sub r6 r3 r2  ; r6 = r3 - r2 (0 - 128 = -128)
    store r6 r2 r3 0x03   ; Store result for inspection

    ; Test AND (Zero flag)
    alu and r7 r1 r3  ; r7 = r1 & r3 (255 & 0 = 0)
    store r7 r2 r3 0x04   ; Store result for inspection

    ; Test XOR (No flags, except Z)
    alu xor r8 r1 r1  ; r8 = r1 ⊕ r1 (255 ⊕ 255 = 0)
    store r8 r2 r3 0x05   ; Store result for inspection

