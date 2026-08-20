import { createRootRoute, Outlet, ScrollRestoration } from "@tanstack/react-router";

export const Route = createRootRoute({
  component: Root,
});

function Root() {
  return (
    <>
      <ScrollRestoration />
      <Outlet />
    </>
  );
}
