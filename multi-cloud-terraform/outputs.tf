cat << EOF > outputs.tf
output "container_ids" {
  description = "IDs of the created containers"
  value       = docker_container.web_app[*].id
}

output "container_names" {
  description = "Names of the created containers"
  value       = docker_container.web_app[*].name
}

output "network_name" {
  description = "Name of the created docker network"
  value       = docker_network.web_network.name
}
EOF
