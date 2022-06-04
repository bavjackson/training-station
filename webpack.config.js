const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: { main: './static/js/main/index.ts' },
  module: {
    rules: [
      {
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  output: {
    path: path.resolve('./static/webpack_bundles/'),
    filename: '[name]-[hash].js',
  },
  plugins: [new BundleTracker({ filename: './webpack-stats.json' })],
};
