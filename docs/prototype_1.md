## User Stories

1. **Task Organization by Class**
   - **As a UVU student**, I want to categorize my tasks by class so I can easily manage and focus on tasks related to specific courses, enhancing my study organization.

2. **Assignment Tracking with Reminders**
   - **As a UVU student**, I need to set reminders for my assignments' due dates to effectively manage my study schedule and ensure I meet all my academic deadlines.

3. **Collaborative Task Lists**
   - **As a UVU student**, I want to share task lists with classmates for group assignments to enhance our collaboration and ensure all parts of the project are completed on time.

4. **Assignment List Creation for Instructors**
   - **As a UVU instructor**, I want to create and share a list of assignments with my students to clarify course expectations and deadlines, supporting their academic success.

5. **Integrated Task Management**
   - **As a member of the UVU community**, I want to manage both my academic and personal tasks in one application to maintain a healthy work-life balance and boost my productivity.

---
---

## Use Cases

1. **Create a Task with Course Tagging**
   - **Actor**: User (Student/Instructor)
   - **Preconditions**: User is logged in, within the CLI application.
   - **Main Flow**: User inputs command to add a task, fills out details including a course tag through CLI prompts, and confirms submission.
   - **Postconditions**: Task is added and categorized under the specified course.

2. **Edit an Existing Task**
   - **Actor**: User
   - **Preconditions**: The task exists.
   - **Main Flow**: User inputs command to edit a task, selects it by identifier, inputs new details or modifications, and confirms changes.
   - **Postconditions**: Task details are updated in the system.

3. **Delete a Task with Confirmation**
   - **Actor**: User
   - **Preconditions**: The task exists.
   - **Main Flow**: User inputs command to delete a task, selects it by identifier, and is prompted for confirmation before deletion.
   - **Postconditions**: Upon confirmation, the task is removed from the system.

4. **Set a Task Reminder**
   - **Actor**: User
   - **Preconditions**: The task exists.
   - **Main Flow**: User inputs command to set a reminder, selects the task by identifier, inputs a date and time for the reminder, and confirms.
   - **Postconditions**: A reminder is set, and the system will notify the user at the specified time.

5. **Organize Tasks into Lists**
   - **Actor**: User
   - **Preconditions**: User is logged in.
   - **Main Flow**: User inputs command to create a new task list, names it (optionally with a course name), and adds tasks to it through CLI prompts.
   - **Postconditions**: A new task list is created, organizing tasks as specified.

6. **Prioritize Tasks**
   - **Actor**: User
   - **Preconditions**: The task exists.
   - **Main Flow**: User inputs command to prioritize a task, selects it by identifier, sets a priority level through CLI prompts, and confirms.
   - **Postconditions**: Task priority is updated in the system.

7. **Collaborative Editing via Export/Import**
   - **Actor**: User
   - **Preconditions**: Task list exists.
   - **Main Flow**: User inputs command to export a task list, saving it to a file. Another user can import this file into their session to view or edit.
   - **Postconditions**: Task lists can be shared and edited collaboratively through file exchange.

8. **Manual Integration with Academic Calendar**
   - **Actor**: User
   - **Preconditions**: User decides to manually add academic dates.
   - **Main Flow**: User inputs command to add academic dates as tasks, providing date and event details through CLI prompts.
   - **Postconditions**: Academic dates are added as tasks, aiding in academic planning.

9. **Task Search**
   - **Actor**: User
   - **Preconditions**: Tasks exist in the system.
   - **Main Flow**: User inputs command to search for tasks, using keywords or filters such as due date or course tag, and views matching tasks.
   - **Postconditions**: User can easily find specific tasks or groups of tasks.

10. **Review Completed Tasks**
    - **Actor**: User
    - **Preconditions**: Completed tasks exist.
    - **Main Flow**: User inputs command to view completed tasks, optionally within a specified time frame, reviewing accomplishments.
    - **Postconditions**: User can reflect on and review completed tasks, supporting productivity assessment.