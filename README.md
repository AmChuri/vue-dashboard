# Coding challenge

Welcome to this fullstack coding challenge. This Readme will guide you through it. It will first present a high level full picture of the project and then scope your task.

In order to run the code that already exists for the frontend and the api, please check out the `api/README.md` and the `frontend/README.md`.

## High Level Description

Our company wants to write a checking tool for internal JSONs that store data. These JSONs are checked, everytime our checking system finds an error, it generates a JSON error object like:
```json
{
    "index": SOME_NUMERIC_INDEX,
    "code": SOME_NUMERIC_ERROR_CODE,
    "text": SOME_TEXT_DESCRIPTION
}
```

We then wrote an API that will get all errors generated so far, seperated by their status. A human operator has to be able to see and understand these errors in order to fix them in the original data. Our company strives to reduce errors to almost zero by providing a flawless UI/UX for operators to check errors and resolve them.

## Your task

Some other developer already wrote an API that delivers errors sorted into the 3 available categories: resolved, unresolved, backlog. Another developer has already started on the frontend, but he only did the bare minimum.

Your tasks are split across the frontend and the api, the main focus lies on data manipulation and UI/UX implementation.

Please check all tasks that you completed. Please document everything that should be documented. For example, if you chose to implement a stretch goal functionality that is not part of the list.

*frontend*
- [ ] Write a UI that allows the operator to:
  - [ ] have an "nice" overview of all errors, it should show `unresolved`, then `resolved` and then `backlog` errors
  - [ ] see the `text` and `code` of each error
  - [ ] resolve each individual `unresolved` error by clicking an individual button
  - [ ] unresolve each individual `resolved` error (e.g., when an error was set to `resolved` by mistake) by clicking an individual button
  - [ ] move an individual backlog error to the bottom of the `unresolved` list of displayed errors, by clicking an individual button
  - [ ] undo his last action. E.g., if he resolved an unresolved error, an `undo` functionality enables him to move it back into the unresolved list of errors. This should work between all lists for * only the last* action of a user

This is the absolute minimum our operators need, in order to resolve errors effectively. If you still have time/if you're still willing, you may start on the `stretch goals` - this will enable our operators to resolve errors *effectively*

*frontend stretch goals*
- [ ] make the UI/UX better
  - [ ] shadows,
  - [ ] click, hover animations (e.g. changing to a darker shade of said color)
  - [ ] notifications
  - [ ] mobile layout
  - [ ] ...
- [ ] make the undo functionality better
  - [ ] the user should be able to undo *all* of his actions
  - [ ] when a user clicks undo, the item that switches lists should be in the same position as before (e.g., if the user resolved an error that was in the middle of the list at position 4, it should also re-appear at position 4 if he undoes this action)

Note: These are in no particular order, start and do whatever you like. If you have a good idea on how to solve one of these problems, it would be a good idea to start with that problem. We appreaciate nice UI/UX implementations, but we also appreaciate efficient and smart data structure/logic implementations.

If you have an additional idea, that would bring our operators forward and is not on this stretch goal list, please feel free to implement that as well, or even just write about it in this or some other file. We also love people that think about their tasks and are able to think like the people whose problems they solve.
