from fastapi import APIRouter, HTTPException, status

from models.task import Task, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks: list[dict] = []


@router.get("", response_model=list[TaskOut])
def get_tasks() -> list[dict]:
    return tasks


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: Task) -> dict:
    new_task = {"id": len(tasks) + 1, **task.model_dump()}
    tasks.append(new_task)
    return new_task


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")
