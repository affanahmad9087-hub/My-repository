; x86-64 Assembly Program for Windows
section .data
    hello db "Hello World", 10, 0
    msg_add db "Addition: 10 + 5 = %d", 10, 0
    msg_sub db "Subtraction: 10 - 5 = %d", 10, 0
    msg_mul db "Multiplication: 10 * 5 = %d", 10, 0
    msg_div db "Division: 10 / 5 = %d", 10, 0

section .text
    global main
    extern printf

main:
    push rbp            ; Save state
    mov rbp, rsp
    sub rsp, 32         ; Mandatory Shadow Space for Windows

    ; Print "Hello World"
    lea rcx, [rel hello]
    call printf
    
    ; Addition: 10 + 5
    lea rcx, [rel msg_add]
    mov rdx, 15         ; Windows uses RDX for 2nd argument
    call printf
    
    ; Subtraction: 10 - 5
    lea rcx, [rel msg_sub]
    mov rdx, 5
    call printf
    
    ; Multiplication: 10 * 5
    lea rcx, [rel msg_mul]
    mov rdx, 50
    call printf
    
    ; Division: 10 / 5
    lea rcx, [rel msg_div]
    mov rdx, 2
    call printf
    
    add rsp, 32         ; Clean up Shadow Space
    xor eax, eax        ; Return 0
    pop rbp
    ret
