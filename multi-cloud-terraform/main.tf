terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "web_network" {
  name = "web-app-network"
}

resource "docker_container" "web_app" {
  count = var.container_count
  image = var.container_image
  name  = "web-app-${count.index + 1}"
  
  networks_advanced {
    name = docker_network.web_network.name
  }

  ports {
    internal = 80
    external = 8080 + count.index
  }
}
