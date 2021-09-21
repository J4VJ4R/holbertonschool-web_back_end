// returns an array of students for a specific city with their new grade
// import getListStudents from './0-get_list_students';
export default function updateStudentGradeByCity(studentList, city, newGrade) {
  const students = studentList.filter((stud) => stud.location === city);
  return students.map((stud) => {
    const student = stud;
    const studGrade = newGrade.filter((grade) => grade.studentId === stud.id);
    if (studGrade.length !== 0) student.grade = studGrade[0].grade;
    else student.grade = 'N/A';
    return stud;
  });
}

/* console.log(updateStudentGradeByCity(getListStudents(), "San Francisco",
[{ studentId: 5, grade: 97 }, { studentId: 1, grade: 86 }]));
console.log(updateStudentGradeByCity(getListStudents(), "San Francisco",
[{ studentId: 5, grade: 97 }])); */
