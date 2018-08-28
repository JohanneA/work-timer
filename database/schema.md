### Database schema

##### Session table
* SessionID, int, primary key,
* Job.Name, String, foreign key
* Date, date
* Time, int (seconds)

##### Job table
* JobID, int, primary key
* Name, String
* Salary, double
