// returns an array of student objects who are located in the given city
// import getListStudents from './0-get_list_students';
export default function getStudentsByLocation(studentList, city) {
  return studentList.filter((stud) => stud.location === city);
}

// console.log(getStudentsByLocation(getListStudents(), 'San Francisco'))
