package main

import (
	"fmt"
	"net/http"
)

// Handler untuk root endpoint
func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}

// Fungsi utama
func main() {
	// Rute untuk endpoint "/"
	http.HandleFunc("/", helloHandler)

	// Menentukan port untuk server
	port := ":8080"
	fmt.Printf("Server berjalan di http://localhost%s\n", port)

	// Menjalankan server
	err := http.ListenAndServe(port, nil)
	if err != nil {
		fmt.Println("Gagal menjalankan server:", err)
	}
}
