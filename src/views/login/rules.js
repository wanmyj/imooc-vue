export const validatePassword = () => {
  return (rule, value, callback) => {
    if (value.length < 6) {
      callback(new Error('no less than 6 length'))
    } else {
      callback()
    }
  }
}
