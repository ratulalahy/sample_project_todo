## User Stories

1. _**As a UVU student**_, I want to organize my tasks by class so that I can focus on specific course requirements without getting overwhelmed.
Assignment Tracking

2. _**As a UVU student**_, I need to set reminders for my assignment due dates so that I can manage my study schedule effectively and meet all my deadlines.

3. _**As a UVU student**_, I want to share task lists with classmates for group assignments so that we can collaborate efficiently and ensure all parts of the project are completed on time.

4. _**As a UVU instructor**_, I want to create a list of assignments and share it with my students so that they are clear about the expectations and deadlines for the course.

5. _**As a member of the UVU community**_, I want to manage both my academic and personal tasks in one place so that I can maintain a healthy work-life balance.


## Use Cases
To adjust the use cases for the UVU TODO GUI-based application, emphasizing a graphical user interface and enhancing the user experience for Utah Valley University students and staff, let's refine and expand upon the original use cases to cover more specific functionalities and scenarios pertinent to the university setting.

#### 1. Create a Task with Course Tagging
- **Actor**: User (Student/Instructor)
- **Preconditions**: User is logged in and has courses listed.
- **Main Flow**: User clicks the "New Task" button, fills out the form with task details including selecting a course tag from a dropdown menu of their current courses, and submits the form.
- **Postconditions**: Task is added to the app, tagged with the selected course for easy filtering.

#### 2. Edit an Existing Task
- **Actor**: User
- **Main Flow**: User selects a task, clicks "Edit", modifies details in a form, including changing the course tag if needed, and saves changes.
- **Postconditions**: Task is updated with new details.

#### 3. Delete a Task with Confirmation
- **Actor**: User
- **Main Flow**: User selects a task, clicks "Delete", and receives a confirmation prompt to avoid accidental deletions. Upon confirming, the task is deleted.
- **Postconditions**: Task is removed, ensuring user confirmation was received.

#### 4. Set a Task Reminder with Notifications
- **Actor**: User
- **Main Flow**: User selects a task, clicks "Set Reminder", chooses a time through a graphical calendar and time picker, and activates the reminder.
- **Postconditions**: System schedules a notification reminder for the task.

#### 5. Organize Tasks into Custom and Course-Specific Lists
- **Actor**: User
- **Preconditions**: Tasks and courses exist.
- **Main Flow**: User creates a new list, either custom or linked to a specific course. Tasks can be added directly to course-specific lists or custom lists for broader categories.
- **Postconditions**: Tasks are organized into the selected list, aiding in segregation by course or category.

#### 6. Prioritize Tasks with Visual Indicators
- **Actor**: User
- **Main Flow**: User selects a task and sets a priority level (e.g., high, medium, low) through a dropdown or visual icons. The task visually reflects this priority in the list.
- **Postconditions**: Task is displayed with an appropriate priority indicator.

#### 7. Collaboratively Edit Shared Task Lists
- **Actor**: User
- **Preconditions**: Task list exists and is sharable.
- **Main Flow**: User shares a task list with other UVU users via email or app invite. Shared users can view and edit tasks within the list.
- **Postconditions**: Collaborative editing of task lists is enabled for group projects or study groups.

#### 8. Integrate with UVU Academic Calendar
- **Actor**: User
- **Preconditions**: User opts in for integration.
- **Main Flow**: User enables syncing with the UVU academic calendar. Important academic dates (e.g., exam schedules, registration deadlines) are automatically added as tasks.
- **Postconditions**: Users receive reminders for academic dates, integrating university schedules directly into their task management.

#### 9. Task Search with Advanced Filters
- **Actor**: User
- **Main Flow**: User enters keywords in the search bar and applies filters (e.g., by course, due date, priority) to refine search results.
- **Postconditions**: User can quickly find specific tasks or sets of tasks matching their criteria.

#### 10. Review and Reflect on Completed Tasks
- **Actor**: User
- **Preconditions**: Completed tasks exist.
- **Main Flow**: User accesses a "Completed" section to review tasks they've completed over a selected time frame, providing a sense of accomplishment and a record for reflection.
- **Postconditions**: User can review and reflect on their completed tasks, aiding in personal productivity assessment.


#### Design Considerations for GUI
- **Usability**: The GUI should be clean, intuitive, and consistent, with a layout that minimizes user effort to perform common tasks.
- **Accessibility**: Include features like keyboard shortcuts, screen reader compatibility, and configurable text sizes to accommodate all users.
- **Responsive Design**: Ensure the GUI adapts gracefully to different screen sizes and resolutions, especially important for users accessing the application across various devices.

#### Adjustments for Constraints and Assumptions
- The development timeline and budget may need to accommodate the additional complexity of designing and implementing a GUI, including the iterative process of user interface design, prototyping, and user testing.
