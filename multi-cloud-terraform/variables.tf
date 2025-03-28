cat << EOF > variables.tf
variable "container_count" {
  description = "Number of container instances"
  type        = number
  default     = 3
}

variable "container_image" {
  description = "Docker image to use"
  type        = string
  default     = "nginx:latest"
}
EOF
