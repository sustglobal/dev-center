# Sust Global Dev Center

This is the home of Sust Global's developer tools, guides and reference documentation. The documentation maintained in this repository is hosted at https://developers.sustglobal.com/. Please start there and come back to this repository as needed to access interactive tools and assets.

Need help? Find a bug? Please [file an issue](https://github.com/sustglobal/dev-center/issues/new) and we'll get back to you.

## GitHub Pages Development

The documentation site is published using [GitHub Pages](https://docs.github.com/en/pages).
Local development depends on having a proper Ruby environment set up.
Documentation is available here:
https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll.

Once you have ruby and bundler installed, you should be able to run the following from `./docs/` and see the
documentation site up at `http://localhost:4000`:

```
bundle install && bundle exec jekyll serve
```
