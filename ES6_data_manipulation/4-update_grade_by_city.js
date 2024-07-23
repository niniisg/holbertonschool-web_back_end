export default function updateStudentGradeByCity(getlist, city, newGrades) {
  return getlist
    .filter((getlist) => getlist.location === city)
    .map((getlist) => {
      const gradeRecord = newGrades.find((grade) => grade.studentId === getlist.id);
      return {
        ...getlist,
        grade: gradeRecord ? gradeRecord.grade : 'N/A',
      };
    });
}
