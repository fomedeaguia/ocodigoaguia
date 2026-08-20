import {
  createRootRoute,
  HeadContent,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@tanstack/react-router";
import appStylesHref from "../styles.css?url";

export const Route = createRootRoute({
  head: () => ({
    meta: [
      { charSet: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { property: "og:site_name", content: "O Código Águia" },
      { property: "og:locale", content: "pt_BR" },
    ],
  }),
  component: Root,
});

export const links = () => [
  {
    rel: "stylesheet",
    href: appStylesHref,
  },
];

function Root() {
  return (
    <html lang="pt-BR">
      <head>
        <HeadContent />
        <link rel="stylesheet" href={appStylesHref} />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}
