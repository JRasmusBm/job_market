module.exports = {
  globals: {
    __PATH_PREFIX__: true,
  },
  parser: "@typescript-eslint/parser",
  extends: ["react-app", "plugin:@typescript-eslint/recommended"],
  plugins: ["@typescript-eslint"],
  rules: { semicolon: ["error", "always"] },
}
