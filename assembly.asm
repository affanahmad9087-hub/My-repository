; x86-64 Assembly Program
; Prints "Hello World" and performs basic math operations

section .data
    hello db "Hello World", 0
    msg_add db "Addition: 10 + 5 = ", 0
    msg_sub db "Subtraction: 10 - 5 = ", 0
    msg_mul db "Multiplication: 10 * 5 = ", 0
    msg_div db "Division: 10 / 5 = ", 0

section .text
    global main
    extern printf

main:
    ; Print "Hello World"
    lea rdi, [rel hello]
    call printf
    
    ; Addition: 10 + 5
    lea rdi, [rel msg_add]
    mov rsi, 15
    xor eax, eax
    call printf
    
    ; Subtraction: 10 - 5
    lea rdi, [rel msg_sub]
    mov rsi, 5
    xor eax, eax
    call printf
    
    ; Multiplication: 10 * 5
    lea rdi, [rel msg_mul]
    mov rsi, 50
    xor eax, eax
    call printf
    
    ; Division: 10 / 5
    lea rdi, [rel msg_div]
    mov rsi, 2
    xor eax, eax
    call printf
    
    xor eax, eax
    ret