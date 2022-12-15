const scanner = require('sonarqube-scanner');
scanner(
  {
    serverUrl: 'http://localhost:9000',
    options: {
      'sonar.login': '99d777f46a8552965fddf740f7db99fb02568414',
      'sonar.sources': './src',
      'sonar.exclusions': '**/__tests__/**',
      'sonar.tests': './src/__tests__',
      'sonar.test.inclusions':
        './src/__tests__/*.test.js,./src/__tests__/**/*.test.ts',
      'sonar.typescript.lcov.reportPaths': 'coverage/lcov.info',
      'sonar.testExecutionReportPaths': 'test-report.xml',
    },
  },
  () => process.exit()
);
