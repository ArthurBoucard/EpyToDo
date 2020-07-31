/*DROP DATABASE IF EXISTS epytodo;
CREATE DATABASE epytodo;
USE epytodo;*/

DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS task;
CREATE TABLE task (
    task_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end timestamp NOT NULL,
    status TEXT CHECK(status IN ('not started', 'in progress', 'done')) NOT NULL DEFAULT 'not started',
    PRIMARY KEY(task_id)
);

DROP TABLE IF EXISTS user_has_id;
CREATE TABLE user_has_id (
    fk_user_id INT NOT NULL,
    fk_task_id INT NOT NULL
);