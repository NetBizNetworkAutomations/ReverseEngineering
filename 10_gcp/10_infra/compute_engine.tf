resource "google_compute_instance" "vscode-server-1" {
    name         = "vscode-server-1"
    machine_type = "e2-medium"
    zone         = "asia-northeast1-a"

    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-11"
        }
    }

    network_interface {
        network = "default"
        access_config {}
    }
}