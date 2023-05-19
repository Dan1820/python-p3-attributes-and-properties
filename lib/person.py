#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "MastiffMastiffPurchasing"
]


class Person:
    def __init__(self, name="Dan", job="Admin"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            print("Name must be string under 25 characters.")
        elif len(name) > 25:
            print("Name must be string under 25 characters.")
        else:
            self._name = name

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("The job must be in the following list of jobs: {job}")

    job = property(get_job, set_job)
