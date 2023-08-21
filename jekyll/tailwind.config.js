module.exports = {
  content: ['./_layouts/**/*.html', './_includes/**/*.html', './**/*.html', './*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        display: "Wix Madefor Display,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji",
      },
      maxWidth: {
        '7xl': '86rem',
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
  ],
};