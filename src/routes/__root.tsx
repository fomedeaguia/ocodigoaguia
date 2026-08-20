import {
  createRootRoute,
  HeadContent,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@tanstack/react-router";
import appStylesHref from "../styles.css?url";

export const Route = createRootRoute({
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
