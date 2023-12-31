module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: '@babel/eslint-parser'
  },
  rules: {
    "vue/multi-word-component-names": "off",
    "no-trailing-spaces": "off",
    "no-console": "off",
    "indent": "off",
    "no-unused-vars": "off",
    "quote-props": "off",
    "no-template-curly-in-string": "off",
    "quotes": "off",
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
  }
}
