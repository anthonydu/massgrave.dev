import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Office Download',
  tagline: 'Open-source Windows and Office activator featuring HWID, Ohook, TSforge, and Online KMS activation methods, along with advanced troubleshooting.',
  favicon: 'img/favicon.ico',
  baseUrl: '/',
  baseUrlIssueBanner: true,
  url: 'https://massgrave.dev',
  organizationName: 'massgravel',
  projectName: 'massgrave.dev',

  onBrokenLinks: 'throw',
  trailingSlash: false,

  future: {
    v4: true,
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [],
      },
    ],
  ],

  markdown:
  ({
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    }
  }),

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      image: 'img/card.png',
      navbar: {
        title: 'Office Download',
        logo: {
          alt: 'Office Download',
          src: 'img/logo.png',
        },
        items: [],
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
