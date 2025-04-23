# FastAPI Microservices — Homework 2 & 3

This repository contains two connected homeworks for the course *Architecture of IT Solutions* at the Ukrainian Catholic University (UCU).  
The goal of both assignments is to explore how to design, implement, and containerize a basic microservice-based system using **FastAPI** and **Podman**.

---

## Homework #2 – REST-Based Microservices with Token Authentication

In this task, we built a modular system consisting of three FastAPI services:

- `client_service.py`: public-facing API secured with token authentication
- `business_service.py`: simulates time-consuming processing
- `db_service.py`: in-memory database service

Each service exposes REST endpoints and is responsible for a part of the logic. The `client_service` orchestrates the interaction between them.

The focus was on:

- Designing clear, single-responsibility microservices
- Implementing token-based access control
- Testing communication between independent Python processes

See: [`README_HM2.md`](./README_HM2.md)

---

## Homework #3 – Containerization with Podman

This task extends Homework #2 by wrapping each microservice in its own container using **Podman** and orchestrating them via **Podman Compose**.

Each service has its own Dockerfile and is launched in a shared virtual network. The user can build, run, and interact with the system using standard Podman commands.

The focus was on:

- Writing Dockerfiles for Python-based microservices
- Building and running images with `podman`
- Creating `podman-compose.yml` to orchestrate the setup
- Testing service health and orchestration from a containerized environment

See: [`README_HM3.md`](./README_HM3.md)

---

## Author

Created by **Yelyzaveta Laveikina**  
Course: *Architecture of IT Solutions*  
Ukrainian Catholic University (UCU)
