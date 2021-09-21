// Returns the sum of all the student ids
// import getListStudents from './0-get_list_students';
export default function getStudentIdsSum(studentList) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  return studentList.reduce(reducer, 0);
}

// console.log(getStudentIdsSum(getListStudents()))
