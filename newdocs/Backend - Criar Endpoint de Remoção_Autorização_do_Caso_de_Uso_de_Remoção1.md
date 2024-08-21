```csharp
namespace Project.Application.UseCases.Brands.DeleteBrand.Behaviors
{
    public class DeleteBrandAuthorizationBehavior : IPipelineBehavior<DeleteBrandCommand, Unit>
    {
        private readonly IAuthorizationService _authorizationService;

        public DeleteBrandAuthorizationBehavior(IAuthorizationService authorizationService)
        {
            _authorizationService = authorizationService;
        }

        public async Task<Unit> Handle(DeleteBrandCommand command, RequestHandlerDelegate<Unit> next, CancellationToken ct = default)
        {
            var user = await _authorizationService.GetUserAsync() ??
                throw new UnauthorizedAccessException("User has no authorization to execute this request!");

            return await next();
        }
    }
}
```